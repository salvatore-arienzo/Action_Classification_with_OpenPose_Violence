import cv2
import matplotlib
import pylab as plt
import numpy as np
import math
import tensorflow as tf
import pandas as pd

from models.config import get_default_configuration
from tensorflow.keras.models import load_model
from models.model import get_model
from models.calculateDistance import calculateDistances
from models.NearestPairResearch import coppiaPiuVicina
from models.NearestPairResearch import inserimentoOrdinato

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

    

def getidClosePeople(persone):
    distMin = distance(persone[0][0], persone[0][1], persone[1][0],persone[1][1])
    idPerson = (persone[0][2], persone[1][2])
    for i in_ range(len(persone)):
        for j in range(i+1,len(persone)):
            dist = distance(persone[i][0], persone[i][1], persone[j][0],persone[j][1])
            if dist < distMin:
                distMin = dist
                idPerson = (persone[i][2], persone[j][2])
    return idPerson
                
            
    

def get_bodyparts(inputpath, nFrame):
    
    weights_path = "weights.h5"
    model = get_model(1.0, 224)
    model.load_weights(weights_path)
    
    df = pd.DataFrame({'idFrame' : [],
                   "Xnose1" : [],"Ynose1" : [],"Xnose2" : [],"Ynose2" : [], 
                   "Xneck1" : [],"Yneck1" : [],"Xneck2" : [],"Yneck2" : [], 
                   "XRshoulder1" : [], "YRshoulder1" : [], "XRshoulder2" : [],"YRshoulder2" : [],
                   "XRelbow1" : [],"YRelbow1" : [],"XRelbow2" : [], "YRelbow2" : [],
                   "XRwrist1" : [],"YRwrist1" : [],"XRwrist2" : [],"YRwrist2" : [],
                   "XLShoulder1" : [],"YLShoulder1" : [],"XLShoulder2" : [],"YLShoulder2" : [],
                   "XLelbow1" : [],"YLelbow1" : [],"XLelbow2" : [],"YLelbow2" : [],
                   "XLwrist1" : [],"YLwrist1" : [],"XLwrist2" : [],"YLwrist2" : [],
                   "XRhip1" : [],"YRhip1" : [],"XRhip2" : [],"YRhip2" : [],
                   "XRknee1" : [],"YRknee1" : [],"XRknee2" : [],"YRknee2" : [],
                   "XRankle1" : [], "YRankle1" : [], "XRankle2" : [], "YRankle2" : [],
                   "XLhip1" : [], "YLhip1" : [], "XLhip2" : [], "YLhip2" : [], 
                   "XLknee1" : [], "YLknee1" : [],"XLknee2" : [],"YLknee2" : [],
                   "XLankle1" : [],"YLankle1" : [],"XLankle2" : [],"YLankle2" : [],
                   "XReye1" : [], "YReye1" : [],"XReye2" : [],"YReye2" : [],
                   "XLeye1" : [],"YLeye1" : [],"XLeye2" : [],"YLeye2" : [],
                   "XRear1" : [],"YRear1" : [],"XRear2" : [],"YRear2" : [],
                   "XLear1" : [],"YLear1" : [],"XLear2" : [],"YLear2" : [],
                   "DistNeckHip1" : [], "DistNeckHip2" : [], 
                   "DistNoseLWrist1" : [],"DistNoseRWrist1" : [],"DistNoseLKnee1" : [],"DistNoseRKnee1" : [],
                   "DistLHipLWrist1" : [],"DistLHipRWrist1" : [],"DistRHipLWrist1" : [],"DistRHipRWrist1" : [],
                   "DistLHipLKnee1" : [],"DistLHipRKnee1" : [],"DistRHipLKnee1" : [],"DistRHipRKnee1" : [],
                   "DistNoseLWrist2" : [],"DistNoseRWrist2" : [],"DistNoseLKnee2" : [],"DistNoseRKnee2" : [],
                   "DistLHipLWrist2" : [],"DistLHipRWrist2" : [],"DistRHipLWrist2" : [],"DistRHipRWrist2" : [],
                   "DistLHipLKnee2" : [],"DistLHipRKnee2" : [],"DistRHipLKnee2" : [],"DistRHipRKnee2" : [],
                   "Violence" : []})
    
    bodyparts = {
        0 : "nose",
        1 : "neck",
        2 : "Rshoulder",
        3 : "Relbow",
        4 : "Rwrist",
        5 : "LShoulder",
        6 : "Lelbow",
        7 : "Lwrist",
        8 : "Rhip",
        9 : "Rknee",
        10 : "Rankle",
        11 : "Lhip",
        12 : "Lknee",
        13 : "Lankle",
        14 : "Reye",
        15 : "Leye",
        16 : "Rear",
        17 : "Lear"
    }
        
    for numFrame in range(nFrame): 
        path = inputpath+ "/img"+str(numFrame)+".jpg" 
        frame= dict()
        people = dict()
        oriImg = cv2.imread(path)
        input_img = oriImg[np.newaxis,...] 
        output_blobs = model.predict(input_img) #generate heatmaps and paf vectors
        heatmap = output_blobs[3]
        heatmap = heatmap[0]
        paf = output_blobs[2] 
        paf = paf[0]
        config = get_default_configuration()
        all_peaks = []
        peak_counter = 0
        thre1 = 0.1
        hashMap = dict() 

        for part_meta in config.body_parts.values():
            map = heatmap[:, :, part_meta.heatmap_idx]    

            map_left = np.zeros(map.shape)
            map_left[1:,:] = map[:-1,:]
            map_right = np.zeros(map.shape)
            map_right[:-1,:] = map[1:,:]
            map_up = np.zeros(map.shape)
            map_up[:,1:] = map[:,:-1]
            map_down = np.zeros(map.shape)
            map_down[:,:-1] = map[:,1:]

            peaks_binary = np.logical_and.reduce((map>=map_left, map>=map_right, map>=map_up, map>=map_down, map > thre1))
            peaks = list(zip(np.nonzero(peaks_binary)[1], np.nonzero(peaks_binary)[0])) # note reverse
            peaks_with_score = [x + (map[x[1],x[0]],) for x in peaks]
            id = range(peak_counter, peak_counter + len(peaks))
            peaks_with_score_and_id = [peaks_with_score[i] + (id[i],) for i in range(len(id))]

            for i in id:
                hashMap[i]=part_meta.body_part.name 

            all_peaks.append(peaks_with_score_and_id)
            peak_counter += len(peaks)
        # find connection in the specified sequence, center 29 is in the position 15
        limbSeq = [[2,3], [2,6], [3,4], [4,5], [6,7], [7,8], [2,9], [9,10], \
                   [10,11], [2,12], [12,13], [13,14], [2,1], [1,15], [15,17], \
                   [1,16], [16,18], [3,17], [6,18]]
        # the middle joints heatmap correpondence
        mapIdx = [[31,32], [39,40], [33,34], [35,36], [41,42], [43,44], [19,20], [21,22], \
                  [23,24], [25,26], [27,28], [29,30], [47,48], [49,50], [53,54], [51,52], \
                  [55,56], [37,38], [45,46]]
        thre2 = 0.05

        connection_all = []
        special_k = []
        mid_num = 10

        for k in range(len(mapIdx)):
            score_mid = paf[:,:,[x-19 for x in mapIdx[k]]]
            candA = all_peaks[limbSeq[k][0]-1]
            candB = all_peaks[limbSeq[k][1]-1]
            nA = len(candA)
            nB = len(candB)
            indexA, indexB = limbSeq[k]
            if(nA != 0 and nB != 0):
                connection_candidate = []
                for i in range(nA):
                    for j in range(nB):
                        vec = np.subtract(candB[j][:2], candA[i][:2])
                        norm = math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
                        # failure case when 2 body parts overlaps
                        if norm == 0:
                            continue
                        vec = np.divide(vec, norm)

                        startend = list(zip(np.linspace(candA[i][0], candB[j][0], num=mid_num), \
                                       np.linspace(candA[i][1], candB[j][1], num=mid_num)))

                        vec_x = np.array([score_mid[int(round(startend[I][1])), int(round(startend[I][0])), 0] \
                                          for I in range(len(startend))])
                        vec_y = np.array([score_mid[int(round(startend[I][1])), int(round(startend[I][0])), 1] \
                                          for I in range(len(startend))])

                        score_midpts = np.multiply(vec_x, vec[0]) + np.multiply(vec_y, vec[1])
                        score_with_dist_prior = sum(score_midpts)/len(score_midpts) + min(0.5*oriImg.shape[0]/norm-1, 0)
                        criterion1 = len(np.nonzero(score_midpts > thre2)[0]) > 0.8 * len(score_midpts)
                        criterion2 = score_with_dist_prior > 0
                        if criterion1 and criterion2:
                            connection_candidate.append([i, j, score_with_dist_prior, score_with_dist_prior+candA[i][2]+candB[j][2]])

                connection_candidate = sorted(connection_candidate, key=lambda x: x[2], reverse=True)
                connection = np.zeros((0,5))
                for c in range(len(connection_candidate)):
                    i,j,s = connection_candidate[c][0:3]
                    if(i not in connection[:,3] and j not in connection[:,4]):
                        connection = np.vstack([connection, [candA[i][3], candB[j][3], s, i, j]])
                        if(len(connection) >= min(nA, nB)):
                            break

                connection_all.append(connection)
            else:
                special_k.append(k)
                connection_all.append([])
        subset = -1 * np.ones((0, 20))
        candidate = np.array([item for sublist in all_peaks for item in sublist])

        for k in range(len(mapIdx)):
            if k not in special_k:
                partAs = connection_all[k][:,0]
                partBs = connection_all[k][:,1]
                indexA, indexB = np.array(limbSeq[k]) - 1

                for i in range(len(connection_all[k])): 
                    found = 0
                    subset_idx = [-1, -1]
                    for j in range(len(subset)): 
                        if subset[j][indexA] == partAs[i] or subset[j][indexB] == partBs[i]:
                            subset_idx[found] = j
                            found += 1

                    if found == 1:
                        j = subset_idx[0]
                        if(subset[j][indexB] != partBs[i]):
                            subset[j][indexB] = partBs[i]
                            subset[j][-1] += 1
                            subset[j][-2] += candidate[partBs[i].astype(int), 2] + connection_all[k][i][2]
                    elif found == 2: # if found 2 and disjoint, merge them
                        j1, j2 = subset_idx
                        membership = ((subset[j1]>=0).astype(int) + (subset[j2]>=0).astype(int))[:-2]
                        if len(np.nonzero(membership == 2)[0]) == 0: #merge
                            subset[j1][:-2] += (subset[j2][:-2] + 1)
                            subset[j1][-2:] += subset[j2][-2:]
                            subset[j1][-2] += connection_all[k][i][2]
                            subset = np.delete(subset, j2, 0)
                        else: # as like found == 1
                            subset[j1][indexB] = partBs[i]
                            subset[j1][-1] += 1
                            subset[j1][-2] += candidate[partBs[i].astype(int), 2] + connection_all[k][i][2]

                    # if find no partA in the subset, create a new subset
                    elif not found and k < 17:
                        row = -1 * np.ones(20)
                        row[indexA] = partAs[i]
                        row[indexB] = partBs[i]
                        row[-1] = 2
                        row[-2] = sum(candidate[connection_all[k][i,:2].astype(int), 2]) + connection_all[k][i][2]
                        subset = np.vstack([subset, row])

        # delete some rows of subset which has few parts occur
        deleteIdx = [];
        for i in range(len(subset)):
            if subset[i][-1] < 4 or subset[i][-2]/subset[i][-1] < 0.4:
                deleteIdx.append(i)
        subset = np.delete(subset, deleteIdx, axis=0)
        scale = 8
        
        if len(subset)>=2:  #Control to check if OpenPose detected 2 people
            
            df.at[len(df)]=0 #Initialize an Empty Row
            df.at[len(df)-1, "idFrame"] = numFrame
            df.at[len(df)-1, "Violence"] = 1 #1 = Non violence, MAKE SURE TO CHANGE TO 0 IF YOU ARE CALCULATING
            coordIdPersonX = []   # VIOLENCE FOLDER BODYPARTS
            coordIdPersonY = []   
            for i in range(len(subset)):
                for j in range(len(subset[i])-2):
                    cella = subset[i][j]
                    if cella != -1:
                        X = candidate[cella.astype(int), 0] * scale
                        Y = candidate[cella.astype(int), 1] * scale
                        #coordIdPerson.append((X,Y,i))
                        inserimentoOrdinato(coordIdPersonX,(X,Y,i),0)
                        inserimentoOrdinato(coordIdPersonY,(X,Y,i),1)
                        break
            idPerson = coppiaPiuVicina(coordIdPersonX,coordIdPersonY, len(coordIdPersonX))
            idPerson1 = idPerson[0][2]
            idPerson2 = idPerson[1][2]
            for j in range(len(subset[idPerson1])-2):
                    cella = subset[idPerson1][j]
                    nomeParte = bodyparts[j] + "1" #Building the string name
                    if cella != -1:
                        X = candidate[cella.astype(int), 0] * scale
                        Y = candidate[cella.astype(int), 1] * scale
                        df.at[len(df)-1,"X"+nomeParte] = X
                        df.at[len(df)-1,"Y"+nomeParte] = Y #Saving Values in the row
                        
            for j in range(len(subset[idPerson2])-2):
                    cella = subset[i][j]
                    nomeParte = bodyparts[j] + "2" #Building the string name
                    if cella != -1:
                        X = candidate[cella.astype(int), 0] * scale
                        Y = candidate[cella.astype(int), 1] * scale
                        df.at[len(df)-1,"X"+nomeParte] = X
                        df.at[len(df)-1,"Y"+nomeParte] = Y #Saving Values in the row
            calculateDistances(df) #Calculating the distance for the single frame
        numFrame= numFrame+1
    return df
        
    
        
        
        
        
        
        
        
        
        
    