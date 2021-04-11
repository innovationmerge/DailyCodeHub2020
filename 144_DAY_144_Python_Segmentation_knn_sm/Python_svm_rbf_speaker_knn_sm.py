# "iNNovationMerge DailyCodeHub"

# Theme : Audio segmentation week with Python

# Fix-sized audio segmentation using pretrained two class KNN model(knn_sm)

from pyAudioAnalysis import audioSegmentation aS

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/knn_sm", "knn", True, 'data/scottish.segments')



