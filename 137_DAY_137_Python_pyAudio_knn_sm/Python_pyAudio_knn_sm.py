# "iNNovationMerge DailyCodeHub"

# Theme : Audio analysis week with Python

# Audio Classification using pretrained two class KNN model(knn_sm)

from pyAudioAnalysis import audioTrainTest as aT

c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/knn_sm","knn")

for k in range(len(p_nam)):
    print(f'P({p_nam[k]}={p[k]})')

    
# Output : 
# P(speech=0.0)
# P(music=1.0)


