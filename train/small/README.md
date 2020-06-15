graph(%input.1 : Float(1, 3, 32, 32),
      %model.bb.conv1.weight : Float(16, 3, 3, 3),
      %model.bb.bn1.weight : Float(16),
      %model.bb.bn1.bias : Float(16),
      %model.bb.bn1.running_mean : Float(16),
      %model.bb.bn1.running_var : Float(16),
      %model.bb.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.0.conv1.weight : Float(16, 16, 1, 1),
      %model.bb.bneck.0.bn1.weight : Float(16),
      %model.bb.bneck.0.bn1.bias : Float(16),
      %model.bb.bneck.0.bn1.running_mean : Float(16),
      %model.bb.bneck.0.bn1.running_var : Float(16),
      %model.bb.bneck.0.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.0.conv2.weight : Float(16, 1, 3, 3),
      %model.bb.bneck.0.bn2.weight : Float(16),
      %model.bb.bneck.0.bn2.bias : Float(16),
      %model.bb.bneck.0.bn2.running_mean : Float(16),
      %model.bb.bneck.0.bn2.running_var : Float(16),
      %model.bb.bneck.0.bn2.num_batches_tracked : Long(),
      %model.bb.bneck.0.conv3.weight : Float(16, 16, 1, 1),
      %model.bb.bneck.0.bn3.weight : Float(16),
      %model.bb.bneck.0.bn3.bias : Float(16),
      %model.bb.bneck.0.bn3.running_mean : Float(16),
      %model.bb.bneck.0.bn3.running_var : Float(16),
      %model.bb.bneck.0.bn3.num_batches_tracked : Long(),
      %model.bb.bneck.1.conv1.weight : Float(72, 16, 1, 1),
      %model.bb.bneck.1.bn1.weight : Float(72),
      %model.bb.bneck.1.bn1.bias : Float(72),
      %model.bb.bneck.1.bn1.running_mean : Float(72),
      %model.bb.bneck.1.bn1.running_var : Float(72),
      %model.bb.bneck.1.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.1.conv2.weight : Float(72, 1, 3, 3),
      %model.bb.bneck.1.bn2.weight : Float(72),
      %model.bb.bneck.1.bn2.bias : Float(72),
      %model.bb.bneck.1.bn2.running_mean : Float(72),
      %model.bb.bneck.1.bn2.running_var : Float(72),
      %model.bb.bneck.1.bn2.num_batches_tracked : Long(),
      %model.bb.bneck.1.conv3.weight : Float(24, 72, 1, 1),
      %model.bb.bneck.1.bn3.weight : Float(24),
      %model.bb.bneck.1.bn3.bias : Float(24),
      %model.bb.bneck.1.bn3.running_mean : Float(24),
      %model.bb.bneck.1.bn3.running_var : Float(24),
      %model.bb.bneck.1.bn3.num_batches_tracked : Long(),
      %model.bb.bneck.2.conv1.weight : Float(88, 24, 1, 1),
      %model.bb.bneck.2.bn1.weight : Float(88),
      %model.bb.bneck.2.bn1.bias : Float(88),
      %model.bb.bneck.2.bn1.running_mean : Float(88),
      %model.bb.bneck.2.bn1.running_var : Float(88),
      %model.bb.bneck.2.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.2.conv2.weight : Float(88, 1, 3, 3),
      %model.bb.bneck.2.bn2.weight : Float(88),
      %model.bb.bneck.2.bn2.bias : Float(88),
      %model.bb.bneck.2.bn2.running_mean : Float(88),
      %model.bb.bneck.2.bn2.running_var : Float(88),
      %model.bb.bneck.2.bn2.num_batches_tracked : Long(),
      %model.bb.bneck.2.conv3.weight : Float(24, 88, 1, 1),
      %model.bb.bneck.2.bn3.weight : Float(24),
      %model.bb.bneck.2.bn3.bias : Float(24),
      %model.bb.bneck.2.bn3.running_mean : Float(24),
      %model.bb.bneck.2.bn3.running_var : Float(24),
      %model.bb.bneck.2.bn3.num_batches_tracked : Long(),
      %model.bb.bneck.3.se.se.0.weight : Float(10, 40, 1, 1),
      %model.bb.bneck.3.se.se.1.weight : Float(10),
      %model.bb.bneck.3.se.se.1.bias : Float(10),
      %model.bb.bneck.3.se.se.1.running_mean : Float(10),
      %model.bb.bneck.3.se.se.1.running_var : Float(10),
      %model.bb.bneck.3.se.se.1.num_batches_tracked : Long(),
      %model.bb.bneck.3.se.se.3.weight : Float(40, 10, 1, 1),
      %model.bb.bneck.3.se.se.4.weight : Float(40),
      %model.bb.bneck.3.se.se.4.bias : Float(40),
      %model.bb.bneck.3.se.se.4.running_mean : Float(40),
      %model.bb.bneck.3.se.se.4.running_var : Float(40),
      %model.bb.bneck.3.se.se.4.num_batches_tracked : Long(),
      %model.bb.bneck.3.conv1.weight : Float(96, 24, 1, 1),
      %model.bb.bneck.3.bn1.weight : Float(96),
      %model.bb.bneck.3.bn1.bias : Float(96),
      %model.bb.bneck.3.bn1.running_mean : Float(96),
      %model.bb.bneck.3.bn1.running_var : Float(96),
      %model.bb.bneck.3.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.3.conv2.weight : Float(96, 1, 5, 5),
      %model.bb.bneck.3.bn2.weight : Float(96),
      %model.bb.bneck.3.bn2.bias : Float(96),
      %model.bb.bneck.3.bn2.running_mean : Float(96),
      %model.bb.bneck.3.bn2.running_var : Float(96),
      %model.bb.bneck.3.bn2.num_batches_tracked : Long(),
      %model.bb.bneck.3.conv3.weight : Float(40, 96, 1, 1),
      %model.bb.bneck.3.bn3.weight : Float(40),
      %model.bb.bneck.3.bn3.bias : Float(40),
      %model.bb.bneck.3.bn3.running_mean : Float(40),
      %model.bb.bneck.3.bn3.running_var : Float(40),
      %model.bb.bneck.3.bn3.num_batches_tracked : Long(),
      %model.bb.bneck.4.se.se.0.weight : Float(10, 40, 1, 1),
      %model.bb.bneck.4.se.se.1.weight : Float(10),
      %model.bb.bneck.4.se.se.1.bias : Float(10),
      %model.bb.bneck.4.se.se.1.running_mean : Float(10),
      %model.bb.bneck.4.se.se.1.running_var : Float(10),
      %model.bb.bneck.4.se.se.1.num_batches_tracked : Long(),
      %model.bb.bneck.4.se.se.3.weight : Float(40, 10, 1, 1),
      %model.bb.bneck.4.se.se.4.weight : Float(40),
      %model.bb.bneck.4.se.se.4.bias : Float(40),
      %model.bb.bneck.4.se.se.4.running_mean : Float(40),
      %model.bb.bneck.4.se.se.4.running_var : Float(40),
      %model.bb.bneck.4.se.se.4.num_batches_tracked : Long(),
      %model.bb.bneck.4.conv1.weight : Float(240, 40, 1, 1),
      %model.bb.bneck.4.bn1.weight : Float(240),
      %model.bb.bneck.4.bn1.bias : Float(240),
      %model.bb.bneck.4.bn1.running_mean : Float(240),
      %model.bb.bneck.4.bn1.running_var : Float(240),
      %model.bb.bneck.4.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.4.conv2.weight : Float(240, 1, 5, 5),
      %model.bb.bneck.4.bn2.weight : Float(240),
      %model.bb.bneck.4.bn2.bias : Float(240),
      %model.bb.bneck.4.bn2.running_mean : Float(240),
      %model.bb.bneck.4.bn2.running_var : Float(240),
      %model.bb.bneck.4.bn2.num_batches_tracked : Long(),
      %model.bb.bneck.4.conv3.weight : Float(40, 240, 1, 1),
      %model.bb.bneck.4.bn3.weight : Float(40),
      %model.bb.bneck.4.bn3.bias : Float(40),
      %model.bb.bneck.4.bn3.running_mean : Float(40),
      %model.bb.bneck.4.bn3.running_var : Float(40),
      %model.bb.bneck.4.bn3.num_batches_tracked : Long(),
      %model.bb.bneck.5.se.se.0.weight : Float(10, 40, 1, 1),
      %model.bb.bneck.5.se.se.1.weight : Float(10),
      %model.bb.bneck.5.se.se.1.bias : Float(10),
      %model.bb.bneck.5.se.se.1.running_mean : Float(10),
      %model.bb.bneck.5.se.se.1.running_var : Float(10),
      %model.bb.bneck.5.se.se.1.num_batches_tracked : Long(),
      %model.bb.bneck.5.se.se.3.weight : Float(40, 10, 1, 1),
      %model.bb.bneck.5.se.se.4.weight : Float(40),
      %model.bb.bneck.5.se.se.4.bias : Float(40),
      %model.bb.bneck.5.se.se.4.running_mean : Float(40),
      %model.bb.bneck.5.se.se.4.running_var : Float(40),
      %model.bb.bneck.5.se.se.4.num_batches_tracked : Long(),
      %model.bb.bneck.5.conv1.weight : Float(240, 40, 1, 1),
      %model.bb.bneck.5.bn1.weight : Float(240),
      %model.bb.bneck.5.bn1.bias : Float(240),
      %model.bb.bneck.5.bn1.running_mean : Float(240),
      %model.bb.bneck.5.bn1.running_var : Float(240),
      %model.bb.bneck.5.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.5.conv2.weight : Float(240, 1, 5, 5),
      %model.bb.bneck.5.bn2.weight : Float(240),
      %model.bb.bneck.5.bn2.bias : Float(240),
      %model.bb.bneck.5.bn2.running_mean : Float(240),
      %model.bb.bneck.5.bn2.running_var : Float(240),
      %model.bb.bneck.5.bn2.num_batches_tracked : Long(),
      %model.bb.bneck.5.conv3.weight : Float(40, 240, 1, 1),
      %model.bb.bneck.5.bn3.weight : Float(40),
      %model.bb.bneck.5.bn3.bias : Float(40),
      %model.bb.bneck.5.bn3.running_mean : Float(40),
      %model.bb.bneck.5.bn3.running_var : Float(40),
      %model.bb.bneck.5.bn3.num_batches_tracked : Long(),
      %model.bb.bneck.6.se.se.0.weight : Float(12, 48, 1, 1),
      %model.bb.bneck.6.se.se.1.weight : Float(12),
      %model.bb.bneck.6.se.se.1.bias : Float(12),
      %model.bb.bneck.6.se.se.1.running_mean : Float(12),
      %model.bb.bneck.6.se.se.1.running_var : Float(12),
      %model.bb.bneck.6.se.se.1.num_batches_tracked : Long(),
      %model.bb.bneck.6.se.se.3.weight : Float(48, 12, 1, 1),
      %model.bb.bneck.6.se.se.4.weight : Float(48),
      %model.bb.bneck.6.se.se.4.bias : Float(48),
      %model.bb.bneck.6.se.se.4.running_mean : Float(48),
      %model.bb.bneck.6.se.se.4.running_var : Float(48),
      %model.bb.bneck.6.se.se.4.num_batches_tracked : Long(),
      %model.bb.bneck.6.conv1.weight : Float(120, 40, 1, 1),
      %model.bb.bneck.6.bn1.weight : Float(120),
      %model.bb.bneck.6.bn1.bias : Float(120),
      %model.bb.bneck.6.bn1.running_mean : Float(120),
      %model.bb.bneck.6.bn1.running_var : Float(120),
      %model.bb.bneck.6.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.6.conv2.weight : Float(120, 1, 5, 5),
      %model.bb.bneck.6.bn2.weight : Float(120),
      %model.bb.bneck.6.bn2.bias : Float(120),
      %model.bb.bneck.6.bn2.running_mean : Float(120),
      %model.bb.bneck.6.bn2.running_var : Float(120),
      %model.bb.bneck.6.bn2.num_batches_tracked : Long(),
      %model.bb.bneck.6.conv3.weight : Float(48, 120, 1, 1),
      %model.bb.bneck.6.bn3.weight : Float(48),
      %model.bb.bneck.6.bn3.bias : Float(48),
      %model.bb.bneck.6.bn3.running_mean : Float(48),
      %model.bb.bneck.6.bn3.running_var : Float(48),
      %model.bb.bneck.6.bn3.num_batches_tracked : Long(),
      %model.bb.bneck.6.shortcut.0.weight : Float(48, 40, 1, 1),
      %model.bb.bneck.6.shortcut.1.weight : Float(48),
      %model.bb.bneck.6.shortcut.1.bias : Float(48),
      %model.bb.bneck.6.shortcut.1.running_mean : Float(48),
      %model.bb.bneck.6.shortcut.1.running_var : Float(48),
      %model.bb.bneck.6.shortcut.1.num_batches_tracked : Long(),
      %model.bb.bneck.7.se.se.0.weight : Float(12, 48, 1, 1),
      %model.bb.bneck.7.se.se.1.weight : Float(12),
      %model.bb.bneck.7.se.se.1.bias : Float(12),
      %model.bb.bneck.7.se.se.1.running_mean : Float(12),
      %model.bb.bneck.7.se.se.1.running_var : Float(12),
      %model.bb.bneck.7.se.se.1.num_batches_tracked : Long(),
      %model.bb.bneck.7.se.se.3.weight : Float(48, 12, 1, 1),
      %model.bb.bneck.7.se.se.4.weight : Float(48),
      %model.bb.bneck.7.se.se.4.bias : Float(48),
      %model.bb.bneck.7.se.se.4.running_mean : Float(48),
      %model.bb.bneck.7.se.se.4.running_var : Float(48),
      %model.bb.bneck.7.se.se.4.num_batches_tracked : Long(),
      %model.bb.bneck.7.conv1.weight : Float(144, 48, 1, 1),
      %model.bb.bneck.7.bn1.weight : Float(144),
      %model.bb.bneck.7.bn1.bias : Float(144),
      %model.bb.bneck.7.bn1.running_mean : Float(144),
      %model.bb.bneck.7.bn1.running_var : Float(144),
      %model.bb.bneck.7.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.7.conv2.weight : Float(144, 1, 5, 5),
      %model.bb.bneck.7.bn2.weight : Float(144),
      %model.bb.bneck.7.bn2.bias : Float(144),
      %model.bb.bneck.7.bn2.running_mean : Float(144),
      %model.bb.bneck.7.bn2.running_var : Float(144),
      %model.bb.bneck.7.bn2.num_batches_tracked : Long(),
      %model.bb.bneck.7.conv3.weight : Float(48, 144, 1, 1),
      %model.bb.bneck.7.bn3.weight : Float(48),
      %model.bb.bneck.7.bn3.bias : Float(48),
      %model.bb.bneck.7.bn3.running_mean : Float(48),
      %model.bb.bneck.7.bn3.running_var : Float(48),
      %model.bb.bneck.7.bn3.num_batches_tracked : Long(),
      %model.bb.bneck.8.se.se.0.weight : Float(24, 96, 1, 1),
      %model.bb.bneck.8.se.se.1.weight : Float(24),
      %model.bb.bneck.8.se.se.1.bias : Float(24),
      %model.bb.bneck.8.se.se.1.running_mean : Float(24),
      %model.bb.bneck.8.se.se.1.running_var : Float(24),
      %model.bb.bneck.8.se.se.1.num_batches_tracked : Long(),
      %model.bb.bneck.8.se.se.3.weight : Float(96, 24, 1, 1),
      %model.bb.bneck.8.se.se.4.weight : Float(96),
      %model.bb.bneck.8.se.se.4.bias : Float(96),
      %model.bb.bneck.8.se.se.4.running_mean : Float(96),
      %model.bb.bneck.8.se.se.4.running_var : Float(96),
      %model.bb.bneck.8.se.se.4.num_batches_tracked : Long(),
      %model.bb.bneck.8.conv1.weight : Float(288, 48, 1, 1),
      %model.bb.bneck.8.bn1.weight : Float(288),
      %model.bb.bneck.8.bn1.bias : Float(288),
      %model.bb.bneck.8.bn1.running_mean : Float(288),
      %model.bb.bneck.8.bn1.running_var : Float(288),
      %model.bb.bneck.8.bn1.num_batches_tracked : Long(),
      %model.bb.bneck.8.conv2.weight : Float(288, 1, 5, 5),
      %model.bb.bneck.8.bn2.weight : Float(288),
      %model.bb.bneck.8.bn2.bias : Float(288),
      %model.bb.bneck.8.bn2.running_mean : Float(288),
      %model.bb.bneck.8.bn2.running_var : Float(288),
      %model.bb.bneck.8.bn2.num_batches_tracked : Long(),
      %model.bb.bneck.8.conv3.weight : Float(96, 288, 1, 1),
      %model.bb.bneck.8.bn3.weight : Float(96),
      %model.bb.bneck.8.bn3.bias : Float(96),
      %model.bb.bneck.8.bn3.running_mean : Float(96),
      %model.bb.bneck.8.bn3.running_var : Float(96),
      %model.bb.bneck.8.bn3.num_batches_tracked : Long(),
      %model.conv3.conv.weight : Float(64, 96, 1, 1),
      %model.conv3.bn.weight : Float(64),
      %model.conv3.bn.bias : Float(64),
      %model.conv3.bn.running_mean : Float(64),
      %model.conv3.bn.running_var : Float(64),
      %model.conv3.bn.num_batches_tracked : Long(),
      %model.connect0.conv.weight : Float(64, 16, 1, 1),
      %model.connect0.bn.weight : Float(64),
      %model.connect0.bn.bias : Float(64),
      %model.connect0.bn.running_mean : Float(64),
      %model.connect0.bn.running_var : Float(64),
      %model.connect0.bn.num_batches_tracked : Long(),
      %model.connect1.conv.weight : Float(64, 24, 1, 1),
      %model.connect1.bn.weight : Float(64),
      %model.connect1.bn.bias : Float(64),
      %model.connect1.bn.running_mean : Float(64),
      %model.connect1.bn.running_var : Float(64),
      %model.connect1.bn.num_batches_tracked : Long(),
      %model.connect2.conv.weight : Float(64, 48, 1, 1),
      %model.connect2.bn.weight : Float(64),
      %model.connect2.bn.bias : Float(64),
      %model.connect2.bn.running_mean : Float(64),
      %model.connect2.bn.running_var : Float(64),
      %model.connect2.bn.num_batches_tracked : Long(),
      %model.up0.conv.conv.weight : Float(64, 64, 3, 3),
      %model.up0.conv.bn.weight : Float(64),
      %model.up0.conv.bn.bias : Float(64),
      %model.up0.conv.bn.running_mean : Float(64),
      %model.up0.conv.bn.running_var : Float(64),
      %model.up0.conv.bn.num_batches_tracked : Long(),
      %model.up1.conv.conv.weight : Float(64, 64, 3, 3),
      %model.up1.conv.bn.weight : Float(64),
      %model.up1.conv.bn.bias : Float(64),
      %model.up1.conv.bn.running_mean : Float(64),
      %model.up1.conv.bn.running_var : Float(64),
      %model.up1.conv.bn.num_batches_tracked : Long(),
      %model.up2.conv.conv.weight : Float(64, 64, 3, 3),
      %model.up2.conv.bn.weight : Float(64),
      %model.up2.conv.bn.bias : Float(64),
      %model.up2.conv.bn.running_mean : Float(64),
      %model.up2.conv.bn.running_var : Float(64),
      %model.up2.conv.bn.num_batches_tracked : Long(),
      %model.detect.upconv.conv.weight : Float(32, 64, 3, 3),
      %model.detect.upconv.bn.weight : Float(32),
      %model.detect.upconv.bn.bias : Float(32),
      %model.detect.upconv.bn.running_mean : Float(32),
      %model.detect.upconv.bn.running_var : Float(32),
      %model.detect.upconv.bn.num_batches_tracked : Long(),
      %model.detect.context.inconv.conv.weight : Float(16, 64, 3, 3),
      %model.detect.context.inconv.bn.weight : Float(16),
      %model.detect.context.inconv.bn.bias : Float(16),
      %model.detect.context.inconv.bn.running_mean : Float(16),
      %model.detect.context.inconv.bn.running_var : Float(16),
      %model.detect.context.inconv.bn.num_batches_tracked : Long(),
      %model.detect.context.upconv.conv.weight : Float(16, 16, 3, 3),
      %model.detect.context.upconv.bn.weight : Float(16),
      %model.detect.context.upconv.bn.bias : Float(16),
      %model.detect.context.upconv.bn.running_mean : Float(16),
      %model.detect.context.upconv.bn.running_var : Float(16),
      %model.detect.context.upconv.bn.num_batches_tracked : Long(),
      %model.detect.context.downconv.conv.weight : Float(16, 16, 3, 3),
      %model.detect.context.downconv.bn.weight : Float(16),
      %model.detect.context.downconv.bn.bias : Float(16),
      %model.detect.context.downconv.bn.running_mean : Float(16),
      %model.detect.context.downconv.bn.running_var : Float(16),
      %model.detect.context.downconv.bn.num_batches_tracked : Long(),
      %model.detect.context.downconv2.conv.weight : Float(16, 16, 3, 3),
      %model.detect.context.downconv2.bn.weight : Float(16),
      %model.detect.context.downconv2.bn.bias : Float(16),
      %model.detect.context.downconv2.bn.running_mean : Float(16),
      %model.detect.context.downconv2.bn.running_var : Float(16),
      %model.detect.context.downconv2.bn.num_batches_tracked : Long(),
      %model.center.head.weight : Float(1, 64, 1, 1),
      %model.center.head.bias : Float(1),
      %model.box.head.weight : Float(4, 64, 1, 1),
      %model.box.head.bias : Float(4),
      %model.landmark.head.weight : Float(10, 64, 1, 1),
      %model.landmark.head.bias : Float(10)):
  %650 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Conv2d[conv1]
  %2294 : int[] = prim::Constant[value=[2, 2]]()
  %2295 : int[] = prim::Constant[value=[1, 1]]()
  %2296 : int[] = prim::Constant[value=[1, 1]]()
  %2552 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Conv2d[conv1]
  %2297 : int[] = prim::Constant[value=[0, 0]]()
  %2553 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Conv2d[conv1]
  %2554 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Conv2d[conv1]
  %2555 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Conv2d[conv1]
  %2556 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Conv2d[conv1]
  %input.2 : Float(1, 16, 16, 16) = aten::_convolution(%input.1, %model.bb.conv1.weight, %650, %2294, %2295, %2296, %2552, %2297, %2553, %2554, %2555, %2556), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2557 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/BatchNorm2d[bn1]
  %2558 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/BatchNorm2d[bn1]
  %2559 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/BatchNorm2d[bn1]
  %2560 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/BatchNorm2d[bn1]
  %input.3 : Float(1, 16, 16, 16) = aten::batch_norm(%input.2, %model.bb.bn1.weight, %model.bb.bn1.bias, %model.bb.bn1.running_mean, %model.bb.bn1.running_var, %2557, %2558, %2559, %2560), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.4 : Float(1, 16, 16, 16) = aten::relu(%input.3), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/ReLU[hs1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %675 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2298 : int[] = prim::Constant[value=[1, 1]]()
  %2299 : int[] = prim::Constant[value=[0, 0]]()
  %2300 : int[] = prim::Constant[value=[1, 1]]()
  %2561 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2301 : int[] = prim::Constant[value=[0, 0]]()
  %2562 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2563 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2564 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2565 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %input.5 : Float(1, 16, 16, 16) = aten::_convolution(%input.4, %model.bb.bneck.0.conv1.weight, %675, %2298, %2299, %2300, %2561, %2301, %2562, %2563, %2564, %2565), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2566 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2567 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2568 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2569 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %input.6 : Float(1, 16, 16, 16) = aten::batch_norm(%input.5, %model.bb.bneck.0.bn1.weight, %model.bb.bneck.0.bn1.bias, %model.bb.bneck.0.bn1.running_mean, %model.bb.bneck.0.bn1.running_var, %2566, %2567, %2568, %2569), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.7 : Float(1, 16, 16, 16) = aten::relu(%input.6), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %700 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2302 : int[] = prim::Constant[value=[2, 2]]()
  %2303 : int[] = prim::Constant[value=[1, 1]]()
  %2304 : int[] = prim::Constant[value=[1, 1]]()
  %2570 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2305 : int[] = prim::Constant[value=[0, 0]]()
  %2571 : Long() = prim::Constant[value={16}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2572 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2573 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2574 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %input.8 : Float(1, 16, 8, 8) = aten::_convolution(%input.7, %model.bb.bneck.0.conv2.weight, %700, %2302, %2303, %2304, %2570, %2305, %2571, %2572, %2573, %2574), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2575 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2576 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2577 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2578 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %input.9 : Float(1, 16, 8, 8) = aten::batch_norm(%input.8, %model.bb.bneck.0.bn2.weight, %model.bb.bneck.0.bn2.bias, %model.bb.bneck.0.bn2.running_mean, %model.bb.bneck.0.bn2.running_var, %2575, %2576, %2577, %2578), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.10 : Float(1, 16, 8, 8) = aten::relu(%input.9), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %725 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2306 : int[] = prim::Constant[value=[1, 1]]()
  %2307 : int[] = prim::Constant[value=[0, 0]]()
  %2308 : int[] = prim::Constant[value=[1, 1]]()
  %2579 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2309 : int[] = prim::Constant[value=[0, 0]]()
  %2580 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2581 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2582 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2583 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %input.11 : Float(1, 16, 8, 8) = aten::_convolution(%input.10, %model.bb.bneck.0.conv3.weight, %725, %2306, %2307, %2308, %2579, %2309, %2580, %2581, %2582, %2583), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2584 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2585 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2586 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2587 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %input.12 : Float(1, 16, 8, 8) = aten::batch_norm(%input.11, %model.bb.bneck.0.bn3.weight, %model.bb.bneck.0.bn3.bias, %model.bb.bneck.0.bn3.running_mean, %model.bb.bneck.0.bn3.running_var, %2584, %2585, %2586, %2587), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %749 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2310 : int[] = prim::Constant[value=[1, 1]]()
  %2311 : int[] = prim::Constant[value=[0, 0]]()
  %2312 : int[] = prim::Constant[value=[1, 1]]()
  %2588 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2313 : int[] = prim::Constant[value=[0, 0]]()
  %2589 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2590 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2591 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2592 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %input.13 : Float(1, 72, 8, 8) = aten::_convolution(%input.12, %model.bb.bneck.1.conv1.weight, %749, %2310, %2311, %2312, %2588, %2313, %2589, %2590, %2591, %2592), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2593 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2594 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2595 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2596 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %input.14 : Float(1, 72, 8, 8) = aten::batch_norm(%input.13, %model.bb.bneck.1.bn1.weight, %model.bb.bneck.1.bn1.bias, %model.bb.bneck.1.bn1.running_mean, %model.bb.bneck.1.bn1.running_var, %2593, %2594, %2595, %2596), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.15 : Float(1, 72, 8, 8) = aten::relu(%input.14), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %774 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2314 : int[] = prim::Constant[value=[2, 2]]()
  %2315 : int[] = prim::Constant[value=[1, 1]]()
  %2316 : int[] = prim::Constant[value=[1, 1]]()
  %2597 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2317 : int[] = prim::Constant[value=[0, 0]]()
  %2598 : Long() = prim::Constant[value={72}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2599 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2600 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2601 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %input.16 : Float(1, 72, 4, 4) = aten::_convolution(%input.15, %model.bb.bneck.1.conv2.weight, %774, %2314, %2315, %2316, %2597, %2317, %2598, %2599, %2600, %2601), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2602 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2603 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2604 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2605 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %input.17 : Float(1, 72, 4, 4) = aten::batch_norm(%input.16, %model.bb.bneck.1.bn2.weight, %model.bb.bneck.1.bn2.bias, %model.bb.bneck.1.bn2.running_mean, %model.bb.bneck.1.bn2.running_var, %2602, %2603, %2604, %2605), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.18 : Float(1, 72, 4, 4) = aten::relu(%input.17), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %799 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2318 : int[] = prim::Constant[value=[1, 1]]()
  %2319 : int[] = prim::Constant[value=[0, 0]]()
  %2320 : int[] = prim::Constant[value=[1, 1]]()
  %2606 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2321 : int[] = prim::Constant[value=[0, 0]]()
  %2607 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2608 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2609 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2610 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %input.19 : Float(1, 24, 4, 4) = aten::_convolution(%input.18, %model.bb.bneck.1.conv3.weight, %799, %2318, %2319, %2320, %2606, %2321, %2607, %2608, %2609, %2610), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2611 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2612 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2613 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2614 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %input.20 : Float(1, 24, 4, 4) = aten::batch_norm(%input.19, %model.bb.bneck.1.bn3.weight, %model.bb.bneck.1.bn3.bias, %model.bb.bneck.1.bn3.running_mean, %model.bb.bneck.1.bn3.running_var, %2611, %2612, %2613, %2614), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %823 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2322 : int[] = prim::Constant[value=[1, 1]]()
  %2323 : int[] = prim::Constant[value=[0, 0]]()
  %2324 : int[] = prim::Constant[value=[1, 1]]()
  %2615 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2325 : int[] = prim::Constant[value=[0, 0]]()
  %2616 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2617 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2618 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2619 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %input.21 : Float(1, 88, 4, 4) = aten::_convolution(%input.20, %model.bb.bneck.2.conv1.weight, %823, %2322, %2323, %2324, %2615, %2325, %2616, %2617, %2618, %2619), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2620 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2621 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2622 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2623 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %input.22 : Float(1, 88, 4, 4) = aten::batch_norm(%input.21, %model.bb.bneck.2.bn1.weight, %model.bb.bneck.2.bn1.bias, %model.bb.bneck.2.bn1.running_mean, %model.bb.bneck.2.bn1.running_var, %2620, %2621, %2622, %2623), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.23 : Float(1, 88, 4, 4) = aten::relu(%input.22), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %848 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2326 : int[] = prim::Constant[value=[1, 1]]()
  %2327 : int[] = prim::Constant[value=[1, 1]]()
  %2328 : int[] = prim::Constant[value=[1, 1]]()
  %2624 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2329 : int[] = prim::Constant[value=[0, 0]]()
  %2625 : Long() = prim::Constant[value={88}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2626 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2627 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2628 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %input.24 : Float(1, 88, 4, 4) = aten::_convolution(%input.23, %model.bb.bneck.2.conv2.weight, %848, %2326, %2327, %2328, %2624, %2329, %2625, %2626, %2627, %2628), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2629 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2630 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2631 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2632 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %input.25 : Float(1, 88, 4, 4) = aten::batch_norm(%input.24, %model.bb.bneck.2.bn2.weight, %model.bb.bneck.2.bn2.bias, %model.bb.bneck.2.bn2.running_mean, %model.bb.bneck.2.bn2.running_var, %2629, %2630, %2631, %2632), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.26 : Float(1, 88, 4, 4) = aten::relu(%input.25), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %873 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2330 : int[] = prim::Constant[value=[1, 1]]()
  %2331 : int[] = prim::Constant[value=[0, 0]]()
  %2332 : int[] = prim::Constant[value=[1, 1]]()
  %2633 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2333 : int[] = prim::Constant[value=[0, 0]]()
  %2634 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2635 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2636 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2637 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %input.27 : Float(1, 24, 4, 4) = aten::_convolution(%input.26, %model.bb.bneck.2.conv3.weight, %873, %2330, %2331, %2332, %2633, %2333, %2634, %2635, %2636, %2637), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2638 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2639 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2640 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2641 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %896 : Float(1, 24, 4, 4) = aten::batch_norm(%input.27, %model.bb.bneck.2.bn3.weight, %model.bb.bneck.2.bn3.bias, %model.bb.bneck.2.bn3.running_mean, %model.bb.bneck.2.bn3.running_var, %2638, %2639, %2640, %2641), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2642 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block
  %input.28 : Float(1, 24, 4, 4) = aten::add(%896, %input.20, %2642), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:59:0
  %899 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2334 : int[] = prim::Constant[value=[1, 1]]()
  %2335 : int[] = prim::Constant[value=[0, 0]]()
  %2336 : int[] = prim::Constant[value=[1, 1]]()
  %2643 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2337 : int[] = prim::Constant[value=[0, 0]]()
  %2644 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2645 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2646 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2647 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %input.29 : Float(1, 96, 4, 4) = aten::_convolution(%input.28, %model.bb.bneck.3.conv1.weight, %899, %2334, %2335, %2336, %2643, %2337, %2644, %2645, %2646, %2647), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2648 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2649 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2650 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2651 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %input.30 : Float(1, 96, 4, 4) = aten::batch_norm(%input.29, %model.bb.bneck.3.bn1.weight, %model.bb.bneck.3.bn1.bias, %model.bb.bneck.3.bn1.running_mean, %model.bb.bneck.3.bn1.running_var, %2648, %2649, %2650, %2651), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.31 : Float(1, 96, 4, 4) = aten::relu(%input.30), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %924 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2338 : int[] = prim::Constant[value=[2, 2]]()
  %2339 : int[] = prim::Constant[value=[2, 2]]()
  %2340 : int[] = prim::Constant[value=[1, 1]]()
  %2652 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2341 : int[] = prim::Constant[value=[0, 0]]()
  %2653 : Long() = prim::Constant[value={96}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2654 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2655 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2656 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %input.32 : Float(1, 96, 2, 2) = aten::_convolution(%input.31, %model.bb.bneck.3.conv2.weight, %924, %2338, %2339, %2340, %2652, %2341, %2653, %2654, %2655, %2656), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2657 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2658 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2659 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2660 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %input.33 : Float(1, 96, 2, 2) = aten::batch_norm(%input.32, %model.bb.bneck.3.bn2.weight, %model.bb.bneck.3.bn2.bias, %model.bb.bneck.3.bn2.running_mean, %model.bb.bneck.3.bn2.running_var, %2657, %2658, %2659, %2660), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.34 : Float(1, 96, 2, 2) = aten::relu(%input.33), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %949 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2342 : int[] = prim::Constant[value=[1, 1]]()
  %2343 : int[] = prim::Constant[value=[0, 0]]()
  %2344 : int[] = prim::Constant[value=[1, 1]]()
  %2661 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2345 : int[] = prim::Constant[value=[0, 0]]()
  %2662 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2663 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2664 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2665 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %input.35 : Float(1, 40, 2, 2) = aten::_convolution(%input.34, %model.bb.bneck.3.conv3.weight, %949, %2342, %2343, %2344, %2661, %2345, %2662, %2663, %2664, %2665), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2666 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2667 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2668 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2669 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %input.36 : Float(1, 40, 2, 2) = aten::batch_norm(%input.35, %model.bb.bneck.3.bn3.weight, %model.bb.bneck.3.bn3.bias, %model.bb.bneck.3.bn3.running_mean, %model.bb.bneck.3.bn3.running_var, %2666, %2667, %2668, %2669), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2346 : int[] = prim::Constant[value=[1, 1]]()
  %input.37 : Float(1, 40, 1, 1) = aten::adaptive_avg_pool2d(%input.36, %2346), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/AdaptiveAvgPool2d[pool] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:768:0
  %989 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2347 : int[] = prim::Constant[value=[1, 1]]()
  %2348 : int[] = prim::Constant[value=[0, 0]]()
  %2349 : int[] = prim::Constant[value=[1, 1]]()
  %2670 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2350 : int[] = prim::Constant[value=[0, 0]]()
  %2671 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2672 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2673 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2674 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %input.38 : Float(1, 10, 1, 1) = aten::_convolution(%input.37, %model.bb.bneck.3.se.se.0.weight, %989, %2347, %2348, %2349, %2670, %2350, %2671, %2672, %2673, %2674), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2675 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2676 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2677 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2678 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %input.39 : Float(1, 10, 1, 1) = aten::batch_norm(%input.38, %model.bb.bneck.3.se.se.1.weight, %model.bb.bneck.3.se.se.1.bias, %model.bb.bneck.3.se.se.1.running_mean, %model.bb.bneck.3.se.se.1.running_var, %2675, %2676, %2677, %2678), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.40 : Float(1, 10, 1, 1) = aten::relu(%input.39), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/ReLU[2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1014 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2351 : int[] = prim::Constant[value=[1, 1]]()
  %2352 : int[] = prim::Constant[value=[0, 0]]()
  %2353 : int[] = prim::Constant[value=[1, 1]]()
  %2679 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2354 : int[] = prim::Constant[value=[0, 0]]()
  %2680 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2681 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2682 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2683 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %input.41 : Float(1, 40, 1, 1) = aten::_convolution(%input.40, %model.bb.bneck.3.se.se.3.weight, %1014, %2351, %2352, %2353, %2679, %2354, %2680, %2681, %2682, %2683), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2684 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2685 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2686 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2687 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %1037 : Float(1, 40, 1, 1) = aten::batch_norm(%input.41, %model.bb.bneck.3.se.se.4.weight, %model.bb.bneck.3.se.se.4.bias, %model.bb.bneck.3.se.se.4.running_mean, %model.bb.bneck.3.se.se.4.running_var, %2684, %2685, %2686, %2687), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1038 : Float(1, 40, 1, 1) = aten::sigmoid(%1037), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Sigmoid[5] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/activation.py:271:0
  %input.42 : Float(1, 40, 2, 2) = aten::mul(%input.36, %1038), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:28:0
  %1040 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2355 : int[] = prim::Constant[value=[1, 1]]()
  %2356 : int[] = prim::Constant[value=[0, 0]]()
  %2357 : int[] = prim::Constant[value=[1, 1]]()
  %2688 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2358 : int[] = prim::Constant[value=[0, 0]]()
  %2689 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2690 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2691 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2692 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %input.43 : Float(1, 240, 2, 2) = aten::_convolution(%input.42, %model.bb.bneck.4.conv1.weight, %1040, %2355, %2356, %2357, %2688, %2358, %2689, %2690, %2691, %2692), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2693 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2694 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2695 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2696 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %input.44 : Float(1, 240, 2, 2) = aten::batch_norm(%input.43, %model.bb.bneck.4.bn1.weight, %model.bb.bneck.4.bn1.bias, %model.bb.bneck.4.bn1.running_mean, %model.bb.bneck.4.bn1.running_var, %2693, %2694, %2695, %2696), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.45 : Float(1, 240, 2, 2) = aten::relu(%input.44), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1065 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2359 : int[] = prim::Constant[value=[1, 1]]()
  %2360 : int[] = prim::Constant[value=[2, 2]]()
  %2361 : int[] = prim::Constant[value=[1, 1]]()
  %2697 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2362 : int[] = prim::Constant[value=[0, 0]]()
  %2698 : Long() = prim::Constant[value={240}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2699 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2700 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2701 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %input.46 : Float(1, 240, 2, 2) = aten::_convolution(%input.45, %model.bb.bneck.4.conv2.weight, %1065, %2359, %2360, %2361, %2697, %2362, %2698, %2699, %2700, %2701), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2702 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2703 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2704 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2705 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %input.47 : Float(1, 240, 2, 2) = aten::batch_norm(%input.46, %model.bb.bneck.4.bn2.weight, %model.bb.bneck.4.bn2.bias, %model.bb.bneck.4.bn2.running_mean, %model.bb.bneck.4.bn2.running_var, %2702, %2703, %2704, %2705), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.48 : Float(1, 240, 2, 2) = aten::relu(%input.47), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1090 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2363 : int[] = prim::Constant[value=[1, 1]]()
  %2364 : int[] = prim::Constant[value=[0, 0]]()
  %2365 : int[] = prim::Constant[value=[1, 1]]()
  %2706 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2366 : int[] = prim::Constant[value=[0, 0]]()
  %2707 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2708 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2709 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2710 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %input.49 : Float(1, 40, 2, 2) = aten::_convolution(%input.48, %model.bb.bneck.4.conv3.weight, %1090, %2363, %2364, %2365, %2706, %2366, %2707, %2708, %2709, %2710), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2711 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2712 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2713 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2714 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %input.50 : Float(1, 40, 2, 2) = aten::batch_norm(%input.49, %model.bb.bneck.4.bn3.weight, %model.bb.bneck.4.bn3.bias, %model.bb.bneck.4.bn3.running_mean, %model.bb.bneck.4.bn3.running_var, %2711, %2712, %2713, %2714), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2367 : int[] = prim::Constant[value=[1, 1]]()
  %input.51 : Float(1, 40, 1, 1) = aten::adaptive_avg_pool2d(%input.50, %2367), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/AdaptiveAvgPool2d[pool] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:768:0
  %1130 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2368 : int[] = prim::Constant[value=[1, 1]]()
  %2369 : int[] = prim::Constant[value=[0, 0]]()
  %2370 : int[] = prim::Constant[value=[1, 1]]()
  %2715 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2371 : int[] = prim::Constant[value=[0, 0]]()
  %2716 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2717 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2718 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2719 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %input.52 : Float(1, 10, 1, 1) = aten::_convolution(%input.51, %model.bb.bneck.4.se.se.0.weight, %1130, %2368, %2369, %2370, %2715, %2371, %2716, %2717, %2718, %2719), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2720 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2721 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2722 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2723 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %input.53 : Float(1, 10, 1, 1) = aten::batch_norm(%input.52, %model.bb.bneck.4.se.se.1.weight, %model.bb.bneck.4.se.se.1.bias, %model.bb.bneck.4.se.se.1.running_mean, %model.bb.bneck.4.se.se.1.running_var, %2720, %2721, %2722, %2723), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.54 : Float(1, 10, 1, 1) = aten::relu(%input.53), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/ReLU[2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1155 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2372 : int[] = prim::Constant[value=[1, 1]]()
  %2373 : int[] = prim::Constant[value=[0, 0]]()
  %2374 : int[] = prim::Constant[value=[1, 1]]()
  %2724 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2375 : int[] = prim::Constant[value=[0, 0]]()
  %2725 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2726 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2727 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2728 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %input.55 : Float(1, 40, 1, 1) = aten::_convolution(%input.54, %model.bb.bneck.4.se.se.3.weight, %1155, %2372, %2373, %2374, %2724, %2375, %2725, %2726, %2727, %2728), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2729 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2730 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2731 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2732 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %1178 : Float(1, 40, 1, 1) = aten::batch_norm(%input.55, %model.bb.bneck.4.se.se.4.weight, %model.bb.bneck.4.se.se.4.bias, %model.bb.bneck.4.se.se.4.running_mean, %model.bb.bneck.4.se.se.4.running_var, %2729, %2730, %2731, %2732), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1179 : Float(1, 40, 1, 1) = aten::sigmoid(%1178), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Sigmoid[5] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/activation.py:271:0
  %1180 : Float(1, 40, 2, 2) = aten::mul(%input.50, %1179), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:28:0
  %2733 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block
  %input.56 : Float(1, 40, 2, 2) = aten::add(%1180, %input.42, %2733), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:59:0
  %1183 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2376 : int[] = prim::Constant[value=[1, 1]]()
  %2377 : int[] = prim::Constant[value=[0, 0]]()
  %2378 : int[] = prim::Constant[value=[1, 1]]()
  %2734 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2379 : int[] = prim::Constant[value=[0, 0]]()
  %2735 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2736 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2737 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2738 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %input.57 : Float(1, 240, 2, 2) = aten::_convolution(%input.56, %model.bb.bneck.5.conv1.weight, %1183, %2376, %2377, %2378, %2734, %2379, %2735, %2736, %2737, %2738), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2739 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2740 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2741 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2742 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %input.58 : Float(1, 240, 2, 2) = aten::batch_norm(%input.57, %model.bb.bneck.5.bn1.weight, %model.bb.bneck.5.bn1.bias, %model.bb.bneck.5.bn1.running_mean, %model.bb.bneck.5.bn1.running_var, %2739, %2740, %2741, %2742), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.59 : Float(1, 240, 2, 2) = aten::relu(%input.58), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1208 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2380 : int[] = prim::Constant[value=[1, 1]]()
  %2381 : int[] = prim::Constant[value=[2, 2]]()
  %2382 : int[] = prim::Constant[value=[1, 1]]()
  %2743 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2383 : int[] = prim::Constant[value=[0, 0]]()
  %2744 : Long() = prim::Constant[value={240}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2745 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2746 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2747 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %input.60 : Float(1, 240, 2, 2) = aten::_convolution(%input.59, %model.bb.bneck.5.conv2.weight, %1208, %2380, %2381, %2382, %2743, %2383, %2744, %2745, %2746, %2747), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2748 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2749 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2750 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2751 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %input.61 : Float(1, 240, 2, 2) = aten::batch_norm(%input.60, %model.bb.bneck.5.bn2.weight, %model.bb.bneck.5.bn2.bias, %model.bb.bneck.5.bn2.running_mean, %model.bb.bneck.5.bn2.running_var, %2748, %2749, %2750, %2751), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.62 : Float(1, 240, 2, 2) = aten::relu(%input.61), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1233 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2384 : int[] = prim::Constant[value=[1, 1]]()
  %2385 : int[] = prim::Constant[value=[0, 0]]()
  %2386 : int[] = prim::Constant[value=[1, 1]]()
  %2752 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2387 : int[] = prim::Constant[value=[0, 0]]()
  %2753 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2754 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2755 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2756 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %input.63 : Float(1, 40, 2, 2) = aten::_convolution(%input.62, %model.bb.bneck.5.conv3.weight, %1233, %2384, %2385, %2386, %2752, %2387, %2753, %2754, %2755, %2756), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2757 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2758 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2759 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2760 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %input.64 : Float(1, 40, 2, 2) = aten::batch_norm(%input.63, %model.bb.bneck.5.bn3.weight, %model.bb.bneck.5.bn3.bias, %model.bb.bneck.5.bn3.running_mean, %model.bb.bneck.5.bn3.running_var, %2757, %2758, %2759, %2760), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2388 : int[] = prim::Constant[value=[1, 1]]()
  %input.65 : Float(1, 40, 1, 1) = aten::adaptive_avg_pool2d(%input.64, %2388), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/AdaptiveAvgPool2d[pool] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:768:0
  %1273 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2389 : int[] = prim::Constant[value=[1, 1]]()
  %2390 : int[] = prim::Constant[value=[0, 0]]()
  %2391 : int[] = prim::Constant[value=[1, 1]]()
  %2761 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2392 : int[] = prim::Constant[value=[0, 0]]()
  %2762 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2763 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2764 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2765 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %input.66 : Float(1, 10, 1, 1) = aten::_convolution(%input.65, %model.bb.bneck.5.se.se.0.weight, %1273, %2389, %2390, %2391, %2761, %2392, %2762, %2763, %2764, %2765), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2766 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2767 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2768 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2769 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %input.67 : Float(1, 10, 1, 1) = aten::batch_norm(%input.66, %model.bb.bneck.5.se.se.1.weight, %model.bb.bneck.5.se.se.1.bias, %model.bb.bneck.5.se.se.1.running_mean, %model.bb.bneck.5.se.se.1.running_var, %2766, %2767, %2768, %2769), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.68 : Float(1, 10, 1, 1) = aten::relu(%input.67), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/ReLU[2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1298 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2393 : int[] = prim::Constant[value=[1, 1]]()
  %2394 : int[] = prim::Constant[value=[0, 0]]()
  %2395 : int[] = prim::Constant[value=[1, 1]]()
  %2770 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2396 : int[] = prim::Constant[value=[0, 0]]()
  %2771 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2772 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2773 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2774 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %input.69 : Float(1, 40, 1, 1) = aten::_convolution(%input.68, %model.bb.bneck.5.se.se.3.weight, %1298, %2393, %2394, %2395, %2770, %2396, %2771, %2772, %2773, %2774), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2775 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2776 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2777 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2778 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %1321 : Float(1, 40, 1, 1) = aten::batch_norm(%input.69, %model.bb.bneck.5.se.se.4.weight, %model.bb.bneck.5.se.se.4.bias, %model.bb.bneck.5.se.se.4.running_mean, %model.bb.bneck.5.se.se.4.running_var, %2775, %2776, %2777, %2778), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1322 : Float(1, 40, 1, 1) = aten::sigmoid(%1321), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Sigmoid[5] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/activation.py:271:0
  %1323 : Float(1, 40, 2, 2) = aten::mul(%input.64, %1322), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:28:0
  %2779 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block
  %input.70 : Float(1, 40, 2, 2) = aten::add(%1323, %input.56, %2779), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:59:0
  %1326 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2397 : int[] = prim::Constant[value=[1, 1]]()
  %2398 : int[] = prim::Constant[value=[0, 0]]()
  %2399 : int[] = prim::Constant[value=[1, 1]]()
  %2780 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2400 : int[] = prim::Constant[value=[0, 0]]()
  %2781 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2782 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2783 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2784 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %input.71 : Float(1, 120, 2, 2) = aten::_convolution(%input.70, %model.bb.bneck.6.conv1.weight, %1326, %2397, %2398, %2399, %2780, %2400, %2781, %2782, %2783, %2784), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2785 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2786 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2787 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2788 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %input.72 : Float(1, 120, 2, 2) = aten::batch_norm(%input.71, %model.bb.bneck.6.bn1.weight, %model.bb.bneck.6.bn1.bias, %model.bb.bneck.6.bn1.running_mean, %model.bb.bneck.6.bn1.running_var, %2785, %2786, %2787, %2788), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.73 : Float(1, 120, 2, 2) = aten::relu(%input.72), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1351 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2401 : int[] = prim::Constant[value=[1, 1]]()
  %2402 : int[] = prim::Constant[value=[2, 2]]()
  %2403 : int[] = prim::Constant[value=[1, 1]]()
  %2789 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2404 : int[] = prim::Constant[value=[0, 0]]()
  %2790 : Long() = prim::Constant[value={120}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2791 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2792 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2793 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %input.74 : Float(1, 120, 2, 2) = aten::_convolution(%input.73, %model.bb.bneck.6.conv2.weight, %1351, %2401, %2402, %2403, %2789, %2404, %2790, %2791, %2792, %2793), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2794 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2795 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2796 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2797 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %input.75 : Float(1, 120, 2, 2) = aten::batch_norm(%input.74, %model.bb.bneck.6.bn2.weight, %model.bb.bneck.6.bn2.bias, %model.bb.bneck.6.bn2.running_mean, %model.bb.bneck.6.bn2.running_var, %2794, %2795, %2796, %2797), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.76 : Float(1, 120, 2, 2) = aten::relu(%input.75), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1376 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2405 : int[] = prim::Constant[value=[1, 1]]()
  %2406 : int[] = prim::Constant[value=[0, 0]]()
  %2407 : int[] = prim::Constant[value=[1, 1]]()
  %2798 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2408 : int[] = prim::Constant[value=[0, 0]]()
  %2799 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2800 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2801 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2802 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %input.77 : Float(1, 48, 2, 2) = aten::_convolution(%input.76, %model.bb.bneck.6.conv3.weight, %1376, %2405, %2406, %2407, %2798, %2408, %2799, %2800, %2801, %2802), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2803 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2804 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2805 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2806 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %input.78 : Float(1, 48, 2, 2) = aten::batch_norm(%input.77, %model.bb.bneck.6.bn3.weight, %model.bb.bneck.6.bn3.bias, %model.bb.bneck.6.bn3.running_mean, %model.bb.bneck.6.bn3.running_var, %2803, %2804, %2805, %2806), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2409 : int[] = prim::Constant[value=[1, 1]]()
  %input.79 : Float(1, 48, 1, 1) = aten::adaptive_avg_pool2d(%input.78, %2409), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/AdaptiveAvgPool2d[pool] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:768:0
  %1416 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2410 : int[] = prim::Constant[value=[1, 1]]()
  %2411 : int[] = prim::Constant[value=[0, 0]]()
  %2412 : int[] = prim::Constant[value=[1, 1]]()
  %2807 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2413 : int[] = prim::Constant[value=[0, 0]]()
  %2808 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2809 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2810 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2811 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %input.80 : Float(1, 12, 1, 1) = aten::_convolution(%input.79, %model.bb.bneck.6.se.se.0.weight, %1416, %2410, %2411, %2412, %2807, %2413, %2808, %2809, %2810, %2811), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2812 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2813 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2814 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2815 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %input.81 : Float(1, 12, 1, 1) = aten::batch_norm(%input.80, %model.bb.bneck.6.se.se.1.weight, %model.bb.bneck.6.se.se.1.bias, %model.bb.bneck.6.se.se.1.running_mean, %model.bb.bneck.6.se.se.1.running_var, %2812, %2813, %2814, %2815), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.82 : Float(1, 12, 1, 1) = aten::relu(%input.81), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/ReLU[2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1441 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2414 : int[] = prim::Constant[value=[1, 1]]()
  %2415 : int[] = prim::Constant[value=[0, 0]]()
  %2416 : int[] = prim::Constant[value=[1, 1]]()
  %2816 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2417 : int[] = prim::Constant[value=[0, 0]]()
  %2817 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2818 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2819 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2820 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %input.83 : Float(1, 48, 1, 1) = aten::_convolution(%input.82, %model.bb.bneck.6.se.se.3.weight, %1441, %2414, %2415, %2416, %2816, %2417, %2817, %2818, %2819, %2820), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2821 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2822 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2823 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2824 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %1464 : Float(1, 48, 1, 1) = aten::batch_norm(%input.83, %model.bb.bneck.6.se.se.4.weight, %model.bb.bneck.6.se.se.4.bias, %model.bb.bneck.6.se.se.4.running_mean, %model.bb.bneck.6.se.se.4.running_var, %2821, %2822, %2823, %2824), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1465 : Float(1, 48, 1, 1) = aten::sigmoid(%1464), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Sigmoid[5] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/activation.py:271:0
  %1466 : Float(1, 48, 2, 2) = aten::mul(%input.78, %1465), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:28:0
  %1467 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/Conv2d[0]
  %2418 : int[] = prim::Constant[value=[1, 1]]()
  %2419 : int[] = prim::Constant[value=[0, 0]]()
  %2420 : int[] = prim::Constant[value=[1, 1]]()
  %2825 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/Conv2d[0]
  %2421 : int[] = prim::Constant[value=[0, 0]]()
  %2826 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/Conv2d[0]
  %2827 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/Conv2d[0]
  %2828 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/Conv2d[0]
  %2829 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/Conv2d[0]
  %input.84 : Float(1, 48, 2, 2) = aten::_convolution(%input.70, %model.bb.bneck.6.shortcut.0.weight, %1467, %2418, %2419, %2420, %2825, %2421, %2826, %2827, %2828, %2829), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/Conv2d[0] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2830 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/BatchNorm2d[1]
  %2831 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/BatchNorm2d[1]
  %2832 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/BatchNorm2d[1]
  %2833 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/BatchNorm2d[1]
  %1490 : Float(1, 48, 2, 2) = aten::batch_norm(%input.84, %model.bb.bneck.6.shortcut.1.weight, %model.bb.bneck.6.shortcut.1.bias, %model.bb.bneck.6.shortcut.1.running_mean, %model.bb.bneck.6.shortcut.1.running_var, %2830, %2831, %2832, %2833), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Sequential[shortcut]/BatchNorm2d[1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2834 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block
  %input.85 : Float(1, 48, 2, 2) = aten::add(%1466, %1490, %2834), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:59:0
  %1493 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2422 : int[] = prim::Constant[value=[1, 1]]()
  %2423 : int[] = prim::Constant[value=[0, 0]]()
  %2424 : int[] = prim::Constant[value=[1, 1]]()
  %2835 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2425 : int[] = prim::Constant[value=[0, 0]]()
  %2836 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2837 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2838 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2839 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %input.86 : Float(1, 144, 2, 2) = aten::_convolution(%input.85, %model.bb.bneck.7.conv1.weight, %1493, %2422, %2423, %2424, %2835, %2425, %2836, %2837, %2838, %2839), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2840 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2841 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2842 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2843 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %input.87 : Float(1, 144, 2, 2) = aten::batch_norm(%input.86, %model.bb.bneck.7.bn1.weight, %model.bb.bneck.7.bn1.bias, %model.bb.bneck.7.bn1.running_mean, %model.bb.bneck.7.bn1.running_var, %2840, %2841, %2842, %2843), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.88 : Float(1, 144, 2, 2) = aten::relu(%input.87), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1518 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2426 : int[] = prim::Constant[value=[1, 1]]()
  %2427 : int[] = prim::Constant[value=[2, 2]]()
  %2428 : int[] = prim::Constant[value=[1, 1]]()
  %2844 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2429 : int[] = prim::Constant[value=[0, 0]]()
  %2845 : Long() = prim::Constant[value={144}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2846 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2847 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2848 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %input.89 : Float(1, 144, 2, 2) = aten::_convolution(%input.88, %model.bb.bneck.7.conv2.weight, %1518, %2426, %2427, %2428, %2844, %2429, %2845, %2846, %2847, %2848), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2849 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2850 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2851 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2852 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %input.90 : Float(1, 144, 2, 2) = aten::batch_norm(%input.89, %model.bb.bneck.7.bn2.weight, %model.bb.bneck.7.bn2.bias, %model.bb.bneck.7.bn2.running_mean, %model.bb.bneck.7.bn2.running_var, %2849, %2850, %2851, %2852), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.91 : Float(1, 144, 2, 2) = aten::relu(%input.90), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1543 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2430 : int[] = prim::Constant[value=[1, 1]]()
  %2431 : int[] = prim::Constant[value=[0, 0]]()
  %2432 : int[] = prim::Constant[value=[1, 1]]()
  %2853 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2433 : int[] = prim::Constant[value=[0, 0]]()
  %2854 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2855 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2856 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2857 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %input.92 : Float(1, 48, 2, 2) = aten::_convolution(%input.91, %model.bb.bneck.7.conv3.weight, %1543, %2430, %2431, %2432, %2853, %2433, %2854, %2855, %2856, %2857), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2858 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2859 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2860 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2861 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %input.93 : Float(1, 48, 2, 2) = aten::batch_norm(%input.92, %model.bb.bneck.7.bn3.weight, %model.bb.bneck.7.bn3.bias, %model.bb.bneck.7.bn3.running_mean, %model.bb.bneck.7.bn3.running_var, %2858, %2859, %2860, %2861), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2434 : int[] = prim::Constant[value=[1, 1]]()
  %input.94 : Float(1, 48, 1, 1) = aten::adaptive_avg_pool2d(%input.93, %2434), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/AdaptiveAvgPool2d[pool] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:768:0
  %1583 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2435 : int[] = prim::Constant[value=[1, 1]]()
  %2436 : int[] = prim::Constant[value=[0, 0]]()
  %2437 : int[] = prim::Constant[value=[1, 1]]()
  %2862 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2438 : int[] = prim::Constant[value=[0, 0]]()
  %2863 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2864 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2865 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2866 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %input.95 : Float(1, 12, 1, 1) = aten::_convolution(%input.94, %model.bb.bneck.7.se.se.0.weight, %1583, %2435, %2436, %2437, %2862, %2438, %2863, %2864, %2865, %2866), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2867 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2868 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2869 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2870 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %input.96 : Float(1, 12, 1, 1) = aten::batch_norm(%input.95, %model.bb.bneck.7.se.se.1.weight, %model.bb.bneck.7.se.se.1.bias, %model.bb.bneck.7.se.se.1.running_mean, %model.bb.bneck.7.se.se.1.running_var, %2867, %2868, %2869, %2870), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.97 : Float(1, 12, 1, 1) = aten::relu(%input.96), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/ReLU[2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1608 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2439 : int[] = prim::Constant[value=[1, 1]]()
  %2440 : int[] = prim::Constant[value=[0, 0]]()
  %2441 : int[] = prim::Constant[value=[1, 1]]()
  %2871 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2442 : int[] = prim::Constant[value=[0, 0]]()
  %2872 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2873 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2874 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2875 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %input.98 : Float(1, 48, 1, 1) = aten::_convolution(%input.97, %model.bb.bneck.7.se.se.3.weight, %1608, %2439, %2440, %2441, %2871, %2442, %2872, %2873, %2874, %2875), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2876 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2877 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2878 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2879 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %1631 : Float(1, 48, 1, 1) = aten::batch_norm(%input.98, %model.bb.bneck.7.se.se.4.weight, %model.bb.bneck.7.se.se.4.bias, %model.bb.bneck.7.se.se.4.running_mean, %model.bb.bneck.7.se.se.4.running_var, %2876, %2877, %2878, %2879), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1632 : Float(1, 48, 1, 1) = aten::sigmoid(%1631), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Sigmoid[5] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/activation.py:271:0
  %1633 : Float(1, 48, 2, 2) = aten::mul(%input.93, %1632), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:28:0
  %2880 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block
  %input.99 : Float(1, 48, 2, 2) = aten::add(%1633, %input.85, %2880), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:59:0
  %1636 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2443 : int[] = prim::Constant[value=[1, 1]]()
  %2444 : int[] = prim::Constant[value=[0, 0]]()
  %2445 : int[] = prim::Constant[value=[1, 1]]()
  %2881 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2446 : int[] = prim::Constant[value=[0, 0]]()
  %2882 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2883 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2884 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %2885 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1]
  %input.100 : Float(1, 288, 2, 2) = aten::_convolution(%input.99, %model.bb.bneck.8.conv1.weight, %1636, %2443, %2444, %2445, %2881, %2446, %2882, %2883, %2884, %2885), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2886 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2887 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2888 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %2889 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1]
  %input.101 : Float(1, 288, 2, 2) = aten::batch_norm(%input.100, %model.bb.bneck.8.bn1.weight, %model.bb.bneck.8.bn1.bias, %model.bb.bneck.8.bn1.running_mean, %model.bb.bneck.8.bn1.running_var, %2886, %2887, %2888, %2889), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.102 : Float(1, 288, 2, 2) = aten::relu(%input.101), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1661 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2447 : int[] = prim::Constant[value=[2, 2]]()
  %2448 : int[] = prim::Constant[value=[2, 2]]()
  %2449 : int[] = prim::Constant[value=[1, 1]]()
  %2890 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2450 : int[] = prim::Constant[value=[0, 0]]()
  %2891 : Long() = prim::Constant[value={288}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2892 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2893 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %2894 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2]
  %input.103 : Float(1, 288, 1, 1) = aten::_convolution(%input.102, %model.bb.bneck.8.conv2.weight, %1661, %2447, %2448, %2449, %2890, %2450, %2891, %2892, %2893, %2894), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2895 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2896 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2897 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %2898 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2]
  %input.104 : Float(1, 288, 1, 1) = aten::batch_norm(%input.103, %model.bb.bneck.8.bn2.weight, %model.bb.bneck.8.bn2.bias, %model.bb.bneck.8.bn2.running_mean, %model.bb.bneck.8.bn2.running_var, %2895, %2896, %2897, %2898), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.105 : Float(1, 288, 1, 1) = aten::relu(%input.104), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/ReLU[nolinear1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1686 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2451 : int[] = prim::Constant[value=[1, 1]]()
  %2452 : int[] = prim::Constant[value=[0, 0]]()
  %2453 : int[] = prim::Constant[value=[1, 1]]()
  %2899 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2454 : int[] = prim::Constant[value=[0, 0]]()
  %2900 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2901 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2902 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %2903 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3]
  %input.106 : Float(1, 96, 1, 1) = aten::_convolution(%input.105, %model.bb.bneck.8.conv3.weight, %1686, %2451, %2452, %2453, %2899, %2454, %2900, %2901, %2902, %2903), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/Conv2d[conv3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2904 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2905 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2906 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %2907 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3]
  %input.107 : Float(1, 96, 1, 1) = aten::batch_norm(%input.106, %model.bb.bneck.8.bn3.weight, %model.bb.bneck.8.bn3.bias, %model.bb.bneck.8.bn3.running_mean, %model.bb.bneck.8.bn3.running_var, %2904, %2905, %2906, %2907), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/BatchNorm2d[bn3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2455 : int[] = prim::Constant[value=[1, 1]]()
  %input.108 : Float(1, 96, 1, 1) = aten::adaptive_avg_pool2d(%input.107, %2455), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/AdaptiveAvgPool2d[pool] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:768:0
  %1726 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2456 : int[] = prim::Constant[value=[1, 1]]()
  %2457 : int[] = prim::Constant[value=[0, 0]]()
  %2458 : int[] = prim::Constant[value=[1, 1]]()
  %2908 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2459 : int[] = prim::Constant[value=[0, 0]]()
  %2909 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2910 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2911 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %2912 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0]
  %input.109 : Float(1, 24, 1, 1) = aten::_convolution(%input.108, %model.bb.bneck.8.se.se.0.weight, %1726, %2456, %2457, %2458, %2908, %2459, %2909, %2910, %2911, %2912), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[0] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2913 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2914 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2915 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %2916 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1]
  %input.110 : Float(1, 24, 1, 1) = aten::batch_norm(%input.109, %model.bb.bneck.8.se.se.1.weight, %model.bb.bneck.8.se.se.1.bias, %model.bb.bneck.8.se.se.1.running_mean, %model.bb.bneck.8.se.se.1.running_var, %2913, %2914, %2915, %2916), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[1] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.111 : Float(1, 24, 1, 1) = aten::relu(%input.110), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/ReLU[2] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1751 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2460 : int[] = prim::Constant[value=[1, 1]]()
  %2461 : int[] = prim::Constant[value=[0, 0]]()
  %2462 : int[] = prim::Constant[value=[1, 1]]()
  %2917 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2463 : int[] = prim::Constant[value=[0, 0]]()
  %2918 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2919 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2920 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %2921 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3]
  %input.112 : Float(1, 96, 1, 1) = aten::_convolution(%input.111, %model.bb.bneck.8.se.se.3.weight, %1751, %2460, %2461, %2462, %2917, %2463, %2918, %2919, %2920, %2921), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Conv2d[3] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2922 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2923 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2924 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %2925 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4]
  %1774 : Float(1, 96, 1, 1) = aten::batch_norm(%input.112, %model.bb.bneck.8.se.se.4.weight, %model.bb.bneck.8.se.se.4.bias, %model.bb.bneck.8.se.se.4.running_mean, %model.bb.bneck.8.se.se.4.running_var, %2922, %2923, %2924, %2925), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/BatchNorm2d[4] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1775 : Float(1, 96, 1, 1) = aten::sigmoid(%1774), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se]/Sequential[se]/Sigmoid[5] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/activation.py:271:0
  %input.113 : Float(1, 96, 1, 1) = aten::mul(%input.107, %1775), scope: OnnxModel/DBFace[model]/Mbv3SmallFast[bb]/Block/SeModule[se] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:28:0
  %1777 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/Conv2d[conv]
  %2464 : int[] = prim::Constant[value=[1, 1]]()
  %2465 : int[] = prim::Constant[value=[0, 0]]()
  %2466 : int[] = prim::Constant[value=[1, 1]]()
  %2926 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/Conv2d[conv]
  %2467 : int[] = prim::Constant[value=[0, 0]]()
  %2927 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/Conv2d[conv]
  %2928 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/Conv2d[conv]
  %2929 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/Conv2d[conv]
  %2930 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/Conv2d[conv]
  %input.114 : Float(1, 64, 1, 1) = aten::_convolution(%input.113, %model.conv3.conv.weight, %1777, %2464, %2465, %2466, %2926, %2467, %2927, %2928, %2929, %2930), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2931 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/BatchNorm2d[bn]
  %2932 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/BatchNorm2d[bn]
  %2933 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/BatchNorm2d[bn]
  %2934 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/BatchNorm2d[bn]
  %input.115 : Float(1, 64, 1, 1) = aten::batch_norm(%input.114, %model.conv3.bn.weight, %model.conv3.bn.bias, %model.conv3.bn.running_mean, %model.conv3.bn.running_var, %2931, %2932, %2933, %2934), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.116 : Float(1, 64, 1, 1) = aten::relu(%input.115), scope: OnnxModel/DBFace[model]/CBAModule[conv3]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %2935 : Long() = prim::Constant[value={2}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %1803 : Long() = aten::size(%input.116, %2935), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2936 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %2937 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %2938 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %1808 : Float() = aten::to(%1803, %2936, %2937, %2938), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2939 : Double() = prim::Constant[value={2}]()
  %2541 : Float() = aten::mul(%1808, %2939)
  %2940 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %2941 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %2942 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %1820 : Float() = aten::to(%2541, %2940, %2941, %2942), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %1821 : Float() = aten::floor(%1820), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2943 : Long() = prim::Constant[value={3}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %1823 : Long() = aten::size(%input.116, %2943), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2944 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %2945 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %2946 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %1828 : Float() = aten::to(%1823, %2944, %2945, %2946), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2947 : Double() = prim::Constant[value={2}]()
  %2543 : Float() = aten::mul(%1828, %2947)
  %2948 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %2949 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %2950 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %1840 : Float() = aten::to(%2543, %2948, %2949, %2950), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %1841 : Float() = aten::floor(%1840), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %1844 : int[] = prim::ListConstruct(%1821, %1841), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %2951 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up]
  %input.117 : Float(1, 64, 2, 2) = aten::upsample_bilinear2d(%input.116, %1844, %2951), scope: OnnxModel/DBFace[model]/UpModule[up0]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2518:0
  %1847 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/Conv2d[conv]
  %2472 : int[] = prim::Constant[value=[1, 1]]()
  %2473 : int[] = prim::Constant[value=[1, 1]]()
  %2474 : int[] = prim::Constant[value=[1, 1]]()
  %2952 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/Conv2d[conv]
  %2475 : int[] = prim::Constant[value=[0, 0]]()
  %2953 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/Conv2d[conv]
  %2954 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/Conv2d[conv]
  %2955 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/Conv2d[conv]
  %2956 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/Conv2d[conv]
  %input.118 : Float(1, 64, 2, 2) = aten::_convolution(%input.117, %model.up0.conv.conv.weight, %1847, %2472, %2473, %2474, %2952, %2475, %2953, %2954, %2955, %2956), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2957 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/BatchNorm2d[bn]
  %2958 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/BatchNorm2d[bn]
  %2959 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/BatchNorm2d[bn]
  %2960 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/BatchNorm2d[bn]
  %input.119 : Float(1, 64, 2, 2) = aten::batch_norm(%input.118, %model.up0.conv.bn.weight, %model.up0.conv.bn.bias, %model.up0.conv.bn.running_mean, %model.up0.conv.bn.running_var, %2957, %2958, %2959, %2960), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1871 : Float(1, 64, 2, 2) = aten::relu(%input.119), scope: OnnxModel/DBFace[model]/UpModule[up0]/CBAModule[conv]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1872 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/Conv2d[conv]
  %2476 : int[] = prim::Constant[value=[1, 1]]()
  %2477 : int[] = prim::Constant[value=[0, 0]]()
  %2478 : int[] = prim::Constant[value=[1, 1]]()
  %2961 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/Conv2d[conv]
  %2479 : int[] = prim::Constant[value=[0, 0]]()
  %2962 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/Conv2d[conv]
  %2963 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/Conv2d[conv]
  %2964 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/Conv2d[conv]
  %2965 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/Conv2d[conv]
  %input.120 : Float(1, 64, 2, 2) = aten::_convolution(%input.99, %model.connect2.conv.weight, %1872, %2476, %2477, %2478, %2961, %2479, %2962, %2963, %2964, %2965), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2966 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/BatchNorm2d[bn]
  %2967 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/BatchNorm2d[bn]
  %2968 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/BatchNorm2d[bn]
  %2969 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/BatchNorm2d[bn]
  %input.121 : Float(1, 64, 2, 2) = aten::batch_norm(%input.120, %model.connect2.bn.weight, %model.connect2.bn.bias, %model.connect2.bn.running_mean, %model.connect2.bn.running_var, %2966, %2967, %2968, %2969), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1896 : Float(1, 64, 2, 2) = aten::relu(%input.121), scope: OnnxModel/DBFace[model]/CBAModule[connect2]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %2970 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]
  %input.122 : Float(1, 64, 2, 2) = aten::add(%1871, %1896, %2970), scope: OnnxModel/DBFace[model] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:258:0
  %2971 : Long() = prim::Constant[value={2}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %1900 : Long() = aten::size(%input.122, %2971), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2972 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %2973 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %2974 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %1905 : Float() = aten::to(%1900, %2972, %2973, %2974), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2975 : Double() = prim::Constant[value={2}]()
  %2545 : Float() = aten::mul(%1905, %2975)
  %2976 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %2977 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %2978 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %1917 : Float() = aten::to(%2545, %2976, %2977, %2978), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %1918 : Float() = aten::floor(%1917), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2979 : Long() = prim::Constant[value={3}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %1920 : Long() = aten::size(%input.122, %2979), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2980 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %2981 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %2982 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %1925 : Float() = aten::to(%1920, %2980, %2981, %2982), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2983 : Double() = prim::Constant[value={2}]()
  %2547 : Float() = aten::mul(%1925, %2983)
  %2984 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %2985 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %2986 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %1937 : Float() = aten::to(%2547, %2984, %2985, %2986), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %1938 : Float() = aten::floor(%1937), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %1941 : int[] = prim::ListConstruct(%1918, %1938), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %2987 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up]
  %input.123 : Float(1, 64, 4, 4) = aten::upsample_bilinear2d(%input.122, %1941, %2987), scope: OnnxModel/DBFace[model]/UpModule[up1]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2518:0
  %1944 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/Conv2d[conv]
  %2484 : int[] = prim::Constant[value=[1, 1]]()
  %2485 : int[] = prim::Constant[value=[1, 1]]()
  %2486 : int[] = prim::Constant[value=[1, 1]]()
  %2988 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/Conv2d[conv]
  %2487 : int[] = prim::Constant[value=[0, 0]]()
  %2989 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/Conv2d[conv]
  %2990 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/Conv2d[conv]
  %2991 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/Conv2d[conv]
  %2992 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/Conv2d[conv]
  %input.124 : Float(1, 64, 4, 4) = aten::_convolution(%input.123, %model.up1.conv.conv.weight, %1944, %2484, %2485, %2486, %2988, %2487, %2989, %2990, %2991, %2992), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2993 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/BatchNorm2d[bn]
  %2994 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/BatchNorm2d[bn]
  %2995 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/BatchNorm2d[bn]
  %2996 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/BatchNorm2d[bn]
  %input.125 : Float(1, 64, 4, 4) = aten::batch_norm(%input.124, %model.up1.conv.bn.weight, %model.up1.conv.bn.bias, %model.up1.conv.bn.running_mean, %model.up1.conv.bn.running_var, %2993, %2994, %2995, %2996), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1968 : Float(1, 64, 4, 4) = aten::relu(%input.125), scope: OnnxModel/DBFace[model]/UpModule[up1]/CBAModule[conv]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %1969 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/Conv2d[conv]
  %2488 : int[] = prim::Constant[value=[1, 1]]()
  %2489 : int[] = prim::Constant[value=[0, 0]]()
  %2490 : int[] = prim::Constant[value=[1, 1]]()
  %2997 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/Conv2d[conv]
  %2491 : int[] = prim::Constant[value=[0, 0]]()
  %2998 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/Conv2d[conv]
  %2999 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/Conv2d[conv]
  %3000 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/Conv2d[conv]
  %3001 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/Conv2d[conv]
  %input.126 : Float(1, 64, 4, 4) = aten::_convolution(%input.28, %model.connect1.conv.weight, %1969, %2488, %2489, %2490, %2997, %2491, %2998, %2999, %3000, %3001), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %3002 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/BatchNorm2d[bn]
  %3003 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/BatchNorm2d[bn]
  %3004 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/BatchNorm2d[bn]
  %3005 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/BatchNorm2d[bn]
  %input.127 : Float(1, 64, 4, 4) = aten::batch_norm(%input.126, %model.connect1.bn.weight, %model.connect1.bn.bias, %model.connect1.bn.running_mean, %model.connect1.bn.running_var, %3002, %3003, %3004, %3005), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %1993 : Float(1, 64, 4, 4) = aten::relu(%input.127), scope: OnnxModel/DBFace[model]/CBAModule[connect1]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %3006 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]
  %input.128 : Float(1, 64, 4, 4) = aten::add(%1968, %1993, %3006), scope: OnnxModel/DBFace[model] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:259:0
  %3007 : Long() = prim::Constant[value={2}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %1997 : Long() = aten::size(%input.128, %3007), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %3008 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %3009 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %3010 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %2002 : Float() = aten::to(%1997, %3008, %3009, %3010), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %3011 : Double() = prim::Constant[value={2}]()
  %2549 : Float() = aten::mul(%2002, %3011)
  %3012 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %3013 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %3014 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %2014 : Float() = aten::to(%2549, %3012, %3013, %3014), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2015 : Float() = aten::floor(%2014), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %3015 : Long() = prim::Constant[value={3}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %2017 : Long() = aten::size(%input.128, %3015), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %3016 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %3017 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %3018 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %2022 : Float() = aten::to(%2017, %3016, %3017, %3018), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %3019 : Double() = prim::Constant[value={2}]()
  %2551 : Float() = aten::mul(%2022, %3019)
  %3020 : Long() = prim::Constant[value={6}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %3021 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %3022 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %2034 : Float() = aten::to(%2551, %3020, %3021, %3022), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2035 : Float() = aten::floor(%2034), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2481:0
  %2038 : int[] = prim::ListConstruct(%2015, %2035), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %3023 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up]
  %input.129 : Float(1, 64, 8, 8) = aten::upsample_bilinear2d(%input.128, %2038, %3023), scope: OnnxModel/DBFace[model]/UpModule[up2]/UpsamplingBilinear2d[up] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:2518:0
  %2041 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/Conv2d[conv]
  %2496 : int[] = prim::Constant[value=[1, 1]]()
  %2497 : int[] = prim::Constant[value=[1, 1]]()
  %2498 : int[] = prim::Constant[value=[1, 1]]()
  %3024 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/Conv2d[conv]
  %2499 : int[] = prim::Constant[value=[0, 0]]()
  %3025 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/Conv2d[conv]
  %3026 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/Conv2d[conv]
  %3027 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/Conv2d[conv]
  %3028 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/Conv2d[conv]
  %input.130 : Float(1, 64, 8, 8) = aten::_convolution(%input.129, %model.up2.conv.conv.weight, %2041, %2496, %2497, %2498, %3024, %2499, %3025, %3026, %3027, %3028), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %3029 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/BatchNorm2d[bn]
  %3030 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/BatchNorm2d[bn]
  %3031 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/BatchNorm2d[bn]
  %3032 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/BatchNorm2d[bn]
  %input.131 : Float(1, 64, 8, 8) = aten::batch_norm(%input.130, %model.up2.conv.bn.weight, %model.up2.conv.bn.bias, %model.up2.conv.bn.running_mean, %model.up2.conv.bn.running_var, %3029, %3030, %3031, %3032), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2065 : Float(1, 64, 8, 8) = aten::relu(%input.131), scope: OnnxModel/DBFace[model]/UpModule[up2]/CBAModule[conv]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %2066 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/Conv2d[conv]
  %2500 : int[] = prim::Constant[value=[1, 1]]()
  %2501 : int[] = prim::Constant[value=[0, 0]]()
  %2502 : int[] = prim::Constant[value=[1, 1]]()
  %3033 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/Conv2d[conv]
  %2503 : int[] = prim::Constant[value=[0, 0]]()
  %3034 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/Conv2d[conv]
  %3035 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/Conv2d[conv]
  %3036 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/Conv2d[conv]
  %3037 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/Conv2d[conv]
  %input.132 : Float(1, 64, 8, 8) = aten::_convolution(%input.12, %model.connect0.conv.weight, %2066, %2500, %2501, %2502, %3033, %2503, %3034, %3035, %3036, %3037), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %3038 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/BatchNorm2d[bn]
  %3039 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/BatchNorm2d[bn]
  %3040 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/BatchNorm2d[bn]
  %3041 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/BatchNorm2d[bn]
  %input.133 : Float(1, 64, 8, 8) = aten::batch_norm(%input.132, %model.connect0.bn.weight, %model.connect0.bn.bias, %model.connect0.bn.running_mean, %model.connect0.bn.running_var, %3038, %3039, %3040, %3041), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2090 : Float(1, 64, 8, 8) = aten::relu(%input.133), scope: OnnxModel/DBFace[model]/CBAModule[connect0]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %3042 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]
  %input.134 : Float(1, 64, 8, 8) = aten::add(%2065, %2090, %3042), scope: OnnxModel/DBFace[model] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:260:0
  %2093 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/Conv2d[conv]
  %2504 : int[] = prim::Constant[value=[1, 1]]()
  %2505 : int[] = prim::Constant[value=[1, 1]]()
  %2506 : int[] = prim::Constant[value=[1, 1]]()
  %3043 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/Conv2d[conv]
  %2507 : int[] = prim::Constant[value=[0, 0]]()
  %3044 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/Conv2d[conv]
  %3045 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/Conv2d[conv]
  %3046 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/Conv2d[conv]
  %3047 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/Conv2d[conv]
  %input.135 : Float(1, 32, 8, 8) = aten::_convolution(%input.134, %model.detect.upconv.conv.weight, %2093, %2504, %2505, %2506, %3043, %2507, %3044, %3045, %3046, %3047), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %3048 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/BatchNorm2d[bn]
  %3049 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/BatchNorm2d[bn]
  %3050 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/BatchNorm2d[bn]
  %3051 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/BatchNorm2d[bn]
  %input.136 : Float(1, 32, 8, 8) = aten::batch_norm(%input.135, %model.detect.upconv.bn.weight, %model.detect.upconv.bn.bias, %model.detect.upconv.bn.running_mean, %model.detect.upconv.bn.running_var, %3048, %3049, %3050, %3051), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2117 : Float(1, 32, 8, 8) = aten::relu(%input.136), scope: OnnxModel/DBFace[model]/DetectModule[detect]/CBAModule[upconv]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %2118 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/Conv2d[conv]
  %2508 : int[] = prim::Constant[value=[1, 1]]()
  %2509 : int[] = prim::Constant[value=[1, 1]]()
  %2510 : int[] = prim::Constant[value=[1, 1]]()
  %3052 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/Conv2d[conv]
  %2511 : int[] = prim::Constant[value=[0, 0]]()
  %3053 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/Conv2d[conv]
  %3054 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/Conv2d[conv]
  %3055 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/Conv2d[conv]
  %3056 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/Conv2d[conv]
  %input.137 : Float(1, 16, 8, 8) = aten::_convolution(%input.134, %model.detect.context.inconv.conv.weight, %2118, %2508, %2509, %2510, %3052, %2511, %3053, %3054, %3055, %3056), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %3057 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/BatchNorm2d[bn]
  %3058 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/BatchNorm2d[bn]
  %3059 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/BatchNorm2d[bn]
  %3060 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/BatchNorm2d[bn]
  %input.138 : Float(1, 16, 8, 8) = aten::batch_norm(%input.137, %model.detect.context.inconv.bn.weight, %model.detect.context.inconv.bn.bias, %model.detect.context.inconv.bn.running_mean, %model.detect.context.inconv.bn.running_var, %3057, %3058, %3059, %3060), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.139 : Float(1, 16, 8, 8) = aten::relu(%input.138), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[inconv]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %2143 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/Conv2d[conv]
  %2512 : int[] = prim::Constant[value=[1, 1]]()
  %2513 : int[] = prim::Constant[value=[1, 1]]()
  %2514 : int[] = prim::Constant[value=[1, 1]]()
  %3061 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/Conv2d[conv]
  %2515 : int[] = prim::Constant[value=[0, 0]]()
  %3062 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/Conv2d[conv]
  %3063 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/Conv2d[conv]
  %3064 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/Conv2d[conv]
  %3065 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/Conv2d[conv]
  %input.140 : Float(1, 16, 8, 8) = aten::_convolution(%input.139, %model.detect.context.upconv.conv.weight, %2143, %2512, %2513, %2514, %3061, %2515, %3062, %3063, %3064, %3065), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %3066 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/BatchNorm2d[bn]
  %3067 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/BatchNorm2d[bn]
  %3068 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/BatchNorm2d[bn]
  %3069 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/BatchNorm2d[bn]
  %input.141 : Float(1, 16, 8, 8) = aten::batch_norm(%input.140, %model.detect.context.upconv.bn.weight, %model.detect.context.upconv.bn.bias, %model.detect.context.upconv.bn.running_mean, %model.detect.context.upconv.bn.running_var, %3066, %3067, %3068, %3069), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2167 : Float(1, 16, 8, 8) = aten::relu(%input.141), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[upconv]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %2168 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/Conv2d[conv]
  %2516 : int[] = prim::Constant[value=[1, 1]]()
  %2517 : int[] = prim::Constant[value=[1, 1]]()
  %2518 : int[] = prim::Constant[value=[1, 1]]()
  %3070 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/Conv2d[conv]
  %2519 : int[] = prim::Constant[value=[0, 0]]()
  %3071 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/Conv2d[conv]
  %3072 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/Conv2d[conv]
  %3073 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/Conv2d[conv]
  %3074 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/Conv2d[conv]
  %input.142 : Float(1, 16, 8, 8) = aten::_convolution(%input.139, %model.detect.context.downconv.conv.weight, %2168, %2516, %2517, %2518, %3070, %2519, %3071, %3072, %3073, %3074), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %3075 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/BatchNorm2d[bn]
  %3076 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/BatchNorm2d[bn]
  %3077 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/BatchNorm2d[bn]
  %3078 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/BatchNorm2d[bn]
  %input.143 : Float(1, 16, 8, 8) = aten::batch_norm(%input.142, %model.detect.context.downconv.bn.weight, %model.detect.context.downconv.bn.bias, %model.detect.context.downconv.bn.running_mean, %model.detect.context.downconv.bn.running_var, %3075, %3076, %3077, %3078), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %input.144 : Float(1, 16, 8, 8) = aten::relu(%input.143), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %2193 : None = prim::Constant(), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/Conv2d[conv]
  %2520 : int[] = prim::Constant[value=[1, 1]]()
  %2521 : int[] = prim::Constant[value=[1, 1]]()
  %2522 : int[] = prim::Constant[value=[1, 1]]()
  %3079 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/Conv2d[conv]
  %2523 : int[] = prim::Constant[value=[0, 0]]()
  %3080 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/Conv2d[conv]
  %3081 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/Conv2d[conv]
  %3082 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/Conv2d[conv]
  %3083 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/Conv2d[conv]
  %input.145 : Float(1, 16, 8, 8) = aten::_convolution(%input.144, %model.detect.context.downconv2.conv.weight, %2193, %2520, %2521, %2522, %3079, %2523, %3080, %3081, %3082, %3083), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/Conv2d[conv] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %3084 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/BatchNorm2d[bn]
  %3085 : Double() = prim::Constant[value={0.1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/BatchNorm2d[bn]
  %3086 : Double() = prim::Constant[value={1e-05}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/BatchNorm2d[bn]
  %3087 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/BatchNorm2d[bn]
  %input.146 : Float(1, 16, 8, 8) = aten::batch_norm(%input.145, %model.detect.context.downconv2.bn.weight, %model.detect.context.downconv2.bn.bias, %model.detect.context.downconv2.bn.running_mean, %model.detect.context.downconv2.bn.running_var, %3084, %3085, %3086, %3087), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/BatchNorm2d[bn] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:1670:0
  %2217 : Float(1, 16, 8, 8) = aten::relu(%input.146), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]/CBAModule[downconv2]/ReLU[act] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:912:0
  %2218 : Tensor[] = prim::ListConstruct(%2167, %2217), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]
  %3088 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context]
  %2220 : Float(1, 32, 8, 8) = aten::cat(%2218, %3088), scope: OnnxModel/DBFace[model]/DetectModule[detect]/ContextModule[context] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:166:0
  %2221 : Tensor[] = prim::ListConstruct(%2117, %2220), scope: OnnxModel/DBFace[model]/DetectModule[detect]
  %3089 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/DetectModule[detect]
  %input : Float(1, 64, 8, 8) = aten::cat(%2221, %3089), scope: OnnxModel/DBFace[model]/DetectModule[detect] # /home/yangna/deepblue/32_face_detect/DBFace/train/small/dbface.py:180:0
  %2524 : int[] = prim::Constant[value=[1, 1]]()
  %2525 : int[] = prim::Constant[value=[0, 0]]()
  %2526 : int[] = prim::Constant[value=[1, 1]]()
  %3090 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/HeadModule[center]/Conv2d[head]
  %2527 : int[] = prim::Constant[value=[0, 0]]()
  %3091 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/HeadModule[center]/Conv2d[head]
  %3092 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/HeadModule[center]/Conv2d[head]
  %3093 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/HeadModule[center]/Conv2d[head]
  %3094 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/HeadModule[center]/Conv2d[head]
  %2241 : Float(1, 1, 8, 8) = aten::_convolution(%input, %model.center.head.weight, %model.center.head.bias, %2524, %2525, %2526, %3090, %2527, %3091, %3092, %3093, %3094), scope: OnnxModel/DBFace[model]/HeadModule[center]/Conv2d[head] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2528 : int[] = prim::Constant[value=[1, 1]]()
  %2529 : int[] = prim::Constant[value=[0, 0]]()
  %2530 : int[] = prim::Constant[value=[1, 1]]()
  %3095 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/HeadModule[box]/Conv2d[head]
  %2531 : int[] = prim::Constant[value=[0, 0]]()
  %3096 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/HeadModule[box]/Conv2d[head]
  %3097 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/HeadModule[box]/Conv2d[head]
  %3098 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/HeadModule[box]/Conv2d[head]
  %3099 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/HeadModule[box]/Conv2d[head]
  %2259 : Float(1, 4, 8, 8) = aten::_convolution(%input, %model.box.head.weight, %model.box.head.bias, %2528, %2529, %2530, %3095, %2531, %3096, %3097, %3098, %3099), scope: OnnxModel/DBFace[model]/HeadModule[box]/Conv2d[head] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2532 : int[] = prim::Constant[value=[1, 1]]()
  %2533 : int[] = prim::Constant[value=[0, 0]]()
  %2534 : int[] = prim::Constant[value=[1, 1]]()
  %3100 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/HeadModule[landmark]/Conv2d[head]
  %2535 : int[] = prim::Constant[value=[0, 0]]()
  %3101 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/HeadModule[landmark]/Conv2d[head]
  %3102 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/HeadModule[landmark]/Conv2d[head]
  %3103 : Long() = prim::Constant[value={0}](), scope: OnnxModel/DBFace[model]/HeadModule[landmark]/Conv2d[head]
  %3104 : Long() = prim::Constant[value={1}](), scope: OnnxModel/DBFace[model]/HeadModule[landmark]/Conv2d[head]
  %2277 : Float(1, 10, 8, 8) = aten::_convolution(%input, %model.landmark.head.weight, %model.landmark.head.bias, %2532, %2533, %2534, %3100, %2535, %3101, %3102, %3103, %3104), scope: OnnxModel/DBFace[model]/HeadModule[landmark]/Conv2d[head] # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/modules/conv.py:342:0
  %2278 : Float(1, 1, 8, 8) = aten::sigmoid(%2241), scope: OnnxModel # /home/yangna/deepblue/32_face_detect/DBFace/train/small/onnx.py:23:0
  %2536 : int[] = prim::Constant[value=[3, 3]]()
  %2537 : int[] = prim::Constant[value=[1, 1]]()
  %2538 : int[] = prim::Constant[value=[1, 1]]()
  %2539 : int[] = prim::Constant[value=[1, 1]]()
  %3105 : Long() = prim::Constant[value={0}](), scope: OnnxModel
  %2292 : Float(1, 1, 8, 8) = aten::max_pool2d(%2278, %2536, %2537, %2538, %2539, %3105), scope: OnnxModel # /home/yangna/yangna/tool/anaconda2/envs/torch130/lib/python3.6/site-packages/torch/nn/functional.py:488:0
  %2293 : Float(1, 4, 8, 8) = aten::exp(%2259), scope: OnnxModel # /home/yangna/deepblue/32_face_detect/DBFace/train/small/onnx.py:25:0
  return (%2278, %2292, %2293, %2277)
