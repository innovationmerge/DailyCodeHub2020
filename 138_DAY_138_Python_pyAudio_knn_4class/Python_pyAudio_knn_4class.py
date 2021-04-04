# "iNNovationMerge DailyCodeHub"

# Theme : Audio analysis week with Python

# Audio Classification using pretrained four class KNN model(knn_4class)

from pyAudioAnalysis import audioTrainTest as aT

c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/knn_4class","knn")

for k in range(len(p_nam)):
    print(f'P({p_nam[k]}={p[k]})')

    
# Output : 
# P(speech=0.07692307692307693)
# P(music=0.07692307692307693)
# P(silence=0.0)
# P(other=0.8461538461538461)
# Audio Classification usi


