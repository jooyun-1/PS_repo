# 보호소 들어올 당시 중성화 x
# 보호소 나갈 당시 중성화
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME FROM ANIMAL_INS I JOIN ANIMAL_OUTS O ON I.ANIMAL_ID=O.ANIMAL_ID where I.SEX_UPON_INTAKE like 'Intact%' and (O.SEX_UPON_OUTCOME like 'Spayed%' or O.SEX_UPON_OUTCOME like 'Neutered%') order by ANIMAL_ID
