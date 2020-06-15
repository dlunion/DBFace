#include "ncnn_centerface.h"


Centerface::Centerface()
{
}

Centerface::~Centerface()
{
}

int Centerface::init(std::string model_path)
{
	std::string param = model_path + "/ncnn/centerface.param";
	std::string bin= model_path + "/ncnn/centerface.bin";
	net.load_param(param.data());
	net.load_model(bin.data());
	return 0;
}

int Centerface::detect(ncnn::Mat & inblob, std::vector<FaceInfo>& faces, int resized_w, int resized_h, float scoreThresh, float nmsThresh)
{
	if (inblob.empty()) {
		 std::cout << "blob is empty ,please check!" << std::endl;
		 return -1;
	}

	image_h = inblob.h;
	image_w = inblob.w;

	scale_w = (float)image_w / (float)resized_w;
	scale_h = (float)image_h / (float)resized_h;

	ncnn::Mat in;

	//scale 
	dynamicScale(resized_w, resized_h);
	ncnn::resize_bilinear(inblob, in, d_w, d_h);

	ncnn::Extractor ex = net.create_extractor();
	ex.input("input.1", in);

	ncnn::Mat heatmap, scale, offset, landmarks;
	ex.extract("537", heatmap);
	ex.extract("538", scale);
	ex.extract("539", offset);
	ex.extract("540", landmarks);


	decode(heatmap, scale,offset, landmarks,faces, scoreThresh,nmsThresh);
	squareBox(faces);
	return 0;
}

void Centerface::nms(std::vector<FaceInfo>& input, std::vector<FaceInfo>& output, float nmsthreshold,int type)
{
	if (input.empty()) {
		return;
	}
	std::sort(input.begin(), input.end(),
		[](const FaceInfo& a, const FaceInfo& b)
		{
			return a.score < b.score;
		});

	float IOU = 0;
	float maxX = 0;
	float maxY = 0;
	float minX = 0;
	float minY = 0;
	std::vector<int> vPick;
	int nPick = 0;
	std::multimap<float, int> vScores;
	const int num_boxes = input.size();
	vPick.resize(num_boxes);
	for (int i = 0; i < num_boxes; ++i) {
		vScores.insert(std::pair<float, int>(input[i].score, i));
	}
	while (vScores.size() > 0) {
		int last = vScores.rbegin()->second;
		vPick[nPick] = last;
		nPick += 1;
		for (std::multimap<float, int>::iterator it = vScores.begin(); it != vScores.end();) {
			int it_idx = it->second;
			maxX = std::max(input.at(it_idx).x1, input.at(last).x1);
			maxY = std::max(input.at(it_idx).y1, input.at(last).y1);
			minX = std::min(input.at(it_idx).x2, input.at(last).x2);
			minY = std::min(input.at(it_idx).y2, input.at(last).y2);
			//maxX1 and maxY1 reuse 
			maxX = ((minX - maxX + 1) > 0) ? (minX - maxX + 1) : 0;
			maxY = ((minY - maxY + 1) > 0) ? (minY - maxY + 1) : 0;
			//IOU reuse for the area of two bbox
			IOU = maxX * maxY;
			if (type==NMS_UNION)
				IOU = IOU / (input.at(it_idx).area + input.at(last).area - IOU);
			else if (type == NMS_MIN) {
				IOU = IOU / ((input.at(it_idx).area < input.at(last).area) ? input.at(it_idx).area : input.at(last).area);
			}
			if (IOU > nmsthreshold) {
				it = vScores.erase(it);
			}
			else {
				it++;
			}
		}
	}

	vPick.resize(nPick);
	output.resize(nPick);
	for (int i = 0; i < nPick; i++) {
		output[i] = input[vPick[i]];
	}
}

void Centerface::decode(ncnn::Mat & heatmap, ncnn::Mat & scale, ncnn::Mat & offset, ncnn::Mat & landmarks, std::vector<FaceInfo>& faces, float scoreThresh, float nmsThresh)
{
	int fea_h = heatmap.h;
	int fea_w = heatmap.w;
	int spacial_size = fea_w*fea_h;

	float *heatmap_ = (float*)(heatmap.data);

	float *scale0 = (float*)(scale.data);
	float *scale1 = scale0 + spacial_size;

	float *offset0 = (float*)(offset.data);
	float *offset1 = offset0 + spacial_size;

	std::vector<int> ids;
	genIds(heatmap_, fea_h, fea_w, scoreThresh, ids);

	std::vector<FaceInfo> faces_tmp;
	for (int i = 0; i < ids.size() / 2; i++) {
		int id_h = ids[2 * i];
		int id_w = ids[2 * i + 1];
		int index = id_h*fea_w + id_w;

		float s0 = std::exp(scale0[index]) * 4;
		float s1 = std::exp(scale1[index]) * 4;
		float o0 = offset0[index];
		float o1 = offset1[index];

		//std::cout << s0 << " " << s1 << " " << o0 << " " << o1 << std::endl;

		float x1 = (id_w + o1 + 0.5) * 4 - s1 / 2 > 0.f ? (id_w + o1 + 0.5) * 4 - s1 / 2 : 0;
		float y1 =(id_h + o0 + 0.5) * 4 - s0 / 2 > 0 ? (id_h + o0 + 0.5) * 4 - s0 / 2 : 0;
		float x2 = 0, y2 = 0;
		x1 = x1 < (float)d_w ? x1 : (float)d_w;
		y1 = y1 < (float)d_h ? y1 : (float)d_h;
		x2 =  x1 + s1 < (float)d_w ? x1 + s1 : (float)d_w;
		y2 = y1 + s0 < (float)d_h ? y1 + s0 : (float)d_h;

		//std::cout << x1 << " " << y1 << " " << x2 << " " << y2 << std::endl;

		FaceInfo facebox;
		facebox.x1 = x1;
		facebox.y1 = y1;
		facebox.x2 = x2;
		facebox.y2 = y2;
		facebox.score = heatmap_[index];
		facebox.area=(facebox.x2-facebox.x1)*(facebox.y2-facebox.y1);


		float box_w = x2 - x1; //=s1?
		float box_h = y2 - y1; //=s0?

		//std::cout << facebox.x1 << " " << facebox.y1 << " " << facebox.x2 << " " << facebox.y2 << std::endl;
		for (int j = 0; j < 5; j++) {
			float *xmap = (float*)landmarks.data + (2 * j + 1)*spacial_size;
			float *ymap = (float*)landmarks.data + (2 * j)*spacial_size;
			facebox.landmarks[2*j] = x1 + xmap[index] * s1;//box_w;
			facebox.landmarks[2 * j+1] = y1 + ymap[index] *  s0; // box_h;
		}
		faces_tmp.push_back(facebox);
	}

	nms(faces_tmp, faces, nmsThresh);

	for (int k = 0; k < faces.size(); k++) {
		faces[k].x1 *= d_scale_w*scale_w;
		faces[k].y1 *= d_scale_h*scale_h;
		faces[k].x2 *= d_scale_w*scale_w;
		faces[k].y2 *= d_scale_h*scale_h;

		for (int kk = 0; kk < 5; kk++) {
			faces[k].landmarks[2*kk]*= d_scale_w*scale_w;
			faces[k].landmarks[2*kk+1] *= d_scale_h*scale_h;
		}
	}
}

void Centerface::dynamicScale(float in_w, float in_h)
{
	d_h = (int)(std::ceil(in_h / 32) * 32);
	d_w = (int)(std::ceil(in_w / 32) * 32);

	d_scale_h = in_h / d_h;
	d_scale_w = in_w / d_w;
}

void Centerface::squareBox(std::vector<FaceInfo>& faces)
{
	float w = 0, h = 0, maxSize = 0;
	float cenx, ceny;
	for (int i = 0; i < faces.size(); i++) {
		w = faces[i].x2 - faces[i].x1;
		h = faces[i].y2 - faces[i].y1;

		maxSize = w < h ? h : w;
		cenx = faces[i].x1 + w / 2;
		ceny = faces[i].y1 + h / 2;

		faces[i].x1 =cenx - maxSize / 2 > 0 ? cenx - maxSize / 2 : 0;
		faces[i].y1 =ceny - maxSize / 2 > 0 ? ceny - maxSize / 2 : 0;
		faces[i].x2 = cenx + maxSize / 2 > image_w - 1 ? image_w - 1 : cenx + maxSize / 2;
		faces[i].y2 =ceny + maxSize / 2 > image_h-1 ? image_h - 1 : ceny + maxSize / 2;
	}
}

void Centerface::genIds(float * heatmap, int h, int w, float thresh, std::vector<int>& ids)
{
	if (heatmap==NULL)
	{
		std::cout << "heatmap is nullptr,please check! " << std::endl;
		return;
	}

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			if (heatmap[i*w + j] > thresh) {
				ids.push_back(i);
				ids.push_back(j);
			}
		}
	}
}
