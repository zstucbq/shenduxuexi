安装依赖库requirement.txt
使用命令python -m pip install -r requirement.txt即可安装。
此时还需要额外安装部分其他库：addict、natsort等，具体看运行代码时的提示。

在官网下载训练集以及测试集，网址：https://tianchi.aliyun.com/competition/entrance/231685/information

下载解压后将训练集和测试集文件拷贝至DBNet.pytorch/datasets文件夹中

在终端中输入
CUDA_VISIBLE_DEVICES=0 python3 tools/train.py --config_file "config/icdar2015_resnet18_FPN_DBhead_polyLR.yaml"
开始训练


训练完成后最优模型保存在DBNet.pytorch/output/DBNet_resnet18_FPN_DBHead/checkpoint/model_best.pth

在终端中输入
CUDA_VISIBLE_DEVICES=0 python3 tools/predict.py --model_path "output/DBNet_resnet18_FPN_DBHead/checkpoint/model_best.pth"
开始对图片进行检测

最后的结果保存在DBNet.pytorch/test/output中