# "iNNovationMerge DailyCodeHub"

# Theme : Audio analysis week with Python

# Audio Classification using pretrained eight class KNN model(knn_movie8class)

from pyAudioAnalysis import audioTrainTest as aT

c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/knn_movie8class","knn")

for k in range(len(p_nam)):
    print(f'P({p_nam[k]}={p[k]})')
    
# Output : 
# P(Speech=0.3333333333333333)
# P(Music=0.5555555555555556)
# P(Others1=0.0)
# P(Others2=0.0)
# P(Others3=0.0)
# P(Shots=0.0)
# P(Fights=0.1111111111111111)
# P(Screams=0.0)



