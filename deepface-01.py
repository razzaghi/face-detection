from deepface import DeepFace

df = DeepFace.find(img_path="sample1.jpg", db_path="./faces")
print(df)
