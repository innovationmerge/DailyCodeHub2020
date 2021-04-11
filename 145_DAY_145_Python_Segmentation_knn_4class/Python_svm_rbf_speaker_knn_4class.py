# "iNNovationMerge DailyCodeHub"

# Theme : Audio segmentation week with Python

# Fix-sized audio segmentation using pretrained four class KNN model(knn_4class)

from pyAudioAnalysis import audioSegmentation aS

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/knn_4class", "knn", True, 'data/scottish.segments')


