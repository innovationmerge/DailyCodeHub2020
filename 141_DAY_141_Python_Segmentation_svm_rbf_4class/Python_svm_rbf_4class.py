# "iNNovationMerge DailyCodeHub"

# Theme : Audio segmentation week with Python

# Fix-sized audio segmentation using pretrained four class SVM model(svm_rbf_4class)

from pyAudioAnalysis import audioSegmentation as aS

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/svm_rbf_4class", "svm", True, 'data/scottish.segments')


