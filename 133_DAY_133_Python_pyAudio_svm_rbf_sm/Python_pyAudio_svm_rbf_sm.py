# "iNNovationMerge DailyCodeHub"

# Theme : Audio analysis week with Python

# Audio Classification using pretrained two class SVM model(svm_rbf_sm)

from pyAudioAnalysis import audioTrainTest as aT

c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/svm_rbf_sm","svm_rbf")

print(f'P({p_nam[0]}={p[0]})')
print(f'P({p_nam[1]}={p[1]})')
    
# Output : 
# P(speech=1.605096086774166e-06)
# P(music=0.9999983949039132)


