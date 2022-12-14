clc,clear;

imdsTrain = imageDatastore(fullfile("img/train/"), ...
    'IncludeSubfolders',true, ...
    'LabelSource','foldernames');

imdsValidation = imageDatastore(fullfile("img/validation/"), ...
    'IncludeSubfolders',true, ...
    'LabelSource','foldernames');

numTrainFiles = 4000;
[imdsTrain,imds_extra1] = splitEachLabel(imdsTrain,numTrainFiles,'randomize');

numValidationFiles = 1000;
[imdsValidation,imds_extra2] = splitEachLabel(imdsValidation,numValidationFiles,'randomize');

labelCount = countEachLabel(imdsTrain);
img = readimage(imdsTrain,1);
size(img);

layers = [
    imageInputLayer([218 178 3])
    
    convolution2dLayer(3,8,'Padding','same')
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,16,'Padding','same')
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,32,'Padding','same')
    batchNormalizationLayer
    reluLayer
    
    fullyConnectedLayer(2)
    softmaxLayer
    classificationLayer];

options = trainingOptions('sgdm', ...
    'InitialLearnRate',0.001, ...
    'MaxEpochs',3, ...
    'Shuffle','every-epoch', ...
    'ValidationData',imdsValidation, ...
    'ValidationFrequency',3, ...
    'Verbose',false, ...
    'Plots','training-progress');
net = trainNetwork(imdsTrain,layers,options);
YPred = classify(net,imdsValidation);
YValidation = imdsValidation.Labels;

accuracy = sum(YPred == YValidation)/numel(YValidation);

imdsTest = imageDatastore(fullfile("img/test/"), ...
    'IncludeSubfolders',true);