# "iNNovationMerge DailyCodeHub"

# Theme : Audio segmentation week with Python

# Fix-sized audio segmentation using pretrained Gender class SVM model(svm_rbf_speaker_male_female)

from pyAudioAnalysis import audioSegmentation aS

[flagsInd, classesAll, acc, CM] = aS.mid_term_file_classification("data/scottish.wav", "data/models/svm_rbf_speaker_male_female", "svm", True, 'data/scottish.segments')


