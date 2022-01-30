from django.shortcuts import render
import numpy as np
import os
# import requests
# from io import BytesIO
from PIL import Image
from math import *
# import efficientnet.tfkeras
# from tensorflow.keras.models import load_model
# import face_recognition
import cv2
from datetime import date, datetime
# Create your views here.

#                     FACE RECOGNITION

def presensi_face(request):
	context = {}
	return render(request, 'dashboard/presensi_face.html', context)

	
# def presensi_face(request):
# 	# context = {}
#     video_capture = cv2.VideoCapture(0)

#     karyawan = Karyawan.objects.all()
#     names = []
#     images = []
#     files = []
#     encodings = []

#     for data in karyawan:
#         names.append(data.nama)
#         files.append('.'+data.foto.url)
#         images.append(data.nama+'_image')
#         encodings.append(data.nama+'_encoding')
    
#     for i in range(0, len(files)):

#         images[i] = face_recognition.load_image_file(files[i])
#         encodings[i] = face_recognition.face_encodings(images[i])[0]

#     known_face_encodings = encodings
#     known_face_names = names
#     counter = 0
#     validate = ''
#     today = date.today()
#     while(video_capture.isOpened()):
#         presensi = Presensi.objects.all()


#         ret, frame = video_capture.read()
#         if(ret):
#             rgb_frame = frame[:, :, ::-1]


#             face_locations = face_recognition.face_locations(rgb_frame)
#             face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             name = "Unknown"
            
#             if True in matches:
#                 first_match_index = matches.index(True)
#                 name = known_face_names[first_match_index]
#                 print(name)

#                 if validate == '':
#                     validate = name
#                 else:
#                     if name == validate:
#                         counter+=1
#                     else:
#                         validate = name
#                         counter = 0

#             print(f'top: {top}, right: {right}, bottom: {bottom}, left: {left}')
#             cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)
#             cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0,0,255), 2)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(frame, name, (left - 50, top - 20), font, 1.0, (255, 255, 255), 1)

#             data = Karyawan.objects.get(nama=name)
#             now = datetime.now()
#             # if now 
#             shift = Shift.objects.get(id_shift=data.shift)
#             if Presensi.objects.filter(nama=name, tanggal=today).exists():
#                 counter = 0
#                 cv2.putText(frame, 'Sudah Presensi', (left - 10, bottom + 40), font, 1.0, (255, 255, 255), 1)
#             else:
#                 if counter >= 3:
#                     data = Karyawan.objects.get(nama=name)
#                     now = datetime.now().strftime('%H:%M:%S')
#                     Presensi(
#                         nip=data.nip,
#                         nama=name,
#                         tanggal=today,
#                         check_in=now,
#                         late_in=now,
#                         check_out=now,
#                         early_out=now,
#                     ).save()
#                     # cv2.putText(frame, 'Sudah Presensi', (left - 10, bottom + 40), font, 1.0, (255, 255, 255), 1)
#                     # counter = 0
                
#         cv2.imshow('Sistem Absensi', rgb_frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     video_capture.release()
#     cv2.destroyAllWindows()
#     return redirect(dashboard)
#     return render(request, 'dashboard/presensi_face.html')