# "iNNovationMerge DailyCodeHub"

# Theme : Audio analysis week with Python

# Audio Classification using pretrained musical class SVM model(svm_rbf_musical_genre_6)

from pyAudioAnalysis import audioTrainTest as aT

c, p, p_nam = aT.file_classification("data/doremi.wav", "data/models/svm_rbf_musical_genre_6","svm")

for k in range(len(p_nam)):
    print(f'P({p_nam[k]}={p[k]})'))

    
# Output : 
# P(Blues=0.19340571058645775)
# P(Classical=0.05183508791839752)
# P(Electronic=0.3333299536117741)
# P(Jazz=0.02182702350701883)
# P(Rap=0.22459715419862877)
# P(Rock=0.17500507017772288)


