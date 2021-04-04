# "iNNovationMerge DailyCodeHub"

# Theme : Audio analysis week with Python

# Audio Classification using pretrained eight class SVM model(svm_rbf_movie8class)

from pyAudioAnalysis import audioTrainTest as aT

c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/svm_rbf_movie8class","svm")

for k in range(len(p_nam)):
    print(f'P({p_nam[k]}={p[k]})')

    
# Output : 
# P(Speech=0.13171912921682888)
# P(Music=0.7011823461550247)
# P(Others1=0.00980347558801528)
# P(Others2=0.020903164965289794)
# P(Others3=0.00724064282867633)
# P(Shots=0.010905822090526755)
# P(Fights=0.018400925456362103)
# P(Screams=0.09984449369927641)


