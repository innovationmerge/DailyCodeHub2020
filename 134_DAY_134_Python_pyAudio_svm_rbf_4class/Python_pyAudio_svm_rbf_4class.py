# "iNNovationMerge DailyCodeHub"

# Theme : Audio analysis week with Python

# Audio Classification using pretrained four class SVM model(svm_rbf_4class)

from pyAudioAnalysis import audioTrainTest as aT

c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/svm_rbf_4class","svm")

print(f'P({p_nam[0]}={p[0]})')
print(f'P({p_nam[1]}={p[1]})')
print(f'P({p_nam[2]}={p[2]})')
print(f'P({p_nam[3]}={p[3]})')
    
# Output : 
# P(speech=0.005759308568885096)
# P(music=0.893296481513386)
# P(silence=0.0016697600146891997)
# P(other=0.0992744499030396)


