import math
import numpy
import pandas

"""
    This class aim to calculate distances between bodyparts. 
    distance(x1,y1,x2,y2) function perform e basic euclidean distance calculation, checking if some of the used 
    values is 0 (missing on the dataset), if so, return 0.
    
    distNeckHip(df)
    distNoseWrist(df)
    distHipWrist(df)
    distHipKnee(df)
    distNoseKnee(df)
    
    These functions perform various calculations between distances:
    distNeckHip(df) calculate the distance between the Neck and the hip of the SAME person, in order to understand if that 
    person is more o less far from the viewpoint. Before to perfrom the operation, we check which values of ankles are 
    available (left or right).
    
    All the other functions are used to calculate the distances between bodyparts of TWO people, with various combination.
    
    Only the most relevant combinations have been chosen.
    
    This functions have been used in the detect_body_parts notebook, in order to populate the dataset.
    
"""

def distance(x1,y1,x2,y2):
    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
        return 0
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def distNeckHip(df):
    
    Xhip = "XRhip1"
    Yhip = "YRhip1"
    if ((df.at[len(df)-1, "XLhip1"] != 0)  or (df.at[len(df)-1, "YLhip1"] != 0)):
        Xhip = "XLhip1"
        Yhip = "YLhip1"
    
    df.at[len(df)-1, "DistNeckHip1"] = distance(df.at[len(df)-1, "Xneck1"],
                                            df.at[len(df)-1, "Yneck1"],
                                            df.at[len(df)-1, Xhip],
                                            df.at[len(df)-1, Yhip])
    Xhip = "XRhip2"
    Yhip = "YRhip2"
    if ((df.at[len(df)-1, "XLhip2"] != 0)  or (df.at[len(df)-1, "YLhip2"] != 0)):
        Xhip = "XLhip2"
        Yhip = "YLhip2"
        
    df.at[len(df)-1, "DistNeckHip2"] = distance(df.at[len(df)-1, "Xneck2"],
                                            df.at[len(df)-1, "Yneck2"],
                                            df.at[len(df)-1, Xhip],
                                            df.at[len(df)-1, Yhip])
    
    
def distNoseWrist(df): 
    
    df.at[len(df)-1, "DistNoseLWrist1"] = distance(df.at[len(df)-1, "Xnose1"],
                                            df.at[len(df)-1, "Ynose1"],
                                            df.at[len(df)-1, "XLwrist2"],
                                            df.at[len(df)-1, "YLwrist2"])
        
    df.at[len(df)-1, "DistNoseRWrist1"] = distance(df.at[len(df)-1, "Xnose1"],
                                            df.at[len(df)-1, "Ynose1"],
                                            df.at[len(df)-1, "XRwrist2"],
                                            df.at[len(df)-1, "YRwrist2"])
    
    df.at[len(df)-1, "DistNoseLWrist2"] = distance(df.at[len(df)-1, "Xnose2"],
                                            df.at[len(df)-1, "Ynose2"],
                                            df.at[len(df)-1, "XLwrist1"],
                                            df.at[len(df)-1, "YLwrist1"])
        
    df.at[len(df)-1, "DistNoseRWrist2"] = distance(df.at[len(df)-1, "Xnose2"],
                                            df.at[len(df)-1, "Ynose2"],
                                            df.at[len(df)-1, "XRwrist1"],
                                            df.at[len(df)-1, "YRwrist1"])
def distNoseKnee(df):
    
    df.at[len(df)-1, "DistNoseLKnee1"] = distance(df.at[len(df)-1, "Xnose1"],
                                            df.at[len(df)-1, "Ynose1"],
                                            df.at[len(df)-1, "XLknee2"],
                                            df.at[len(df)-1, "YLknee2"])
    
    df.at[len(df)-1, "DistNoseRKnee1"] = distance(df.at[len(df)-1, "Xnose1"],
                                            df.at[len(df)-1, "Ynose1"],
                                            df.at[len(df)-1, "XRknee2"],
                                            df.at[len(df)-1, "YRknee2"])
    
    df.at[len(df)-1, "DistNoseLKnee2"] = distance(df.at[len(df)-1, "Xnose2"],
                                            df.at[len(df)-1, "Ynose2"],
                                            df.at[len(df)-1, "XLknee1"],
                                            df.at[len(df)-1, "YLknee1"])
    
    df.at[len(df)-1, "DistNoseRKnee2"] = distance(df.at[len(df)-1, "Xnose2"],
                                            df.at[len(df)-1, "Ynose2"],
                                            df.at[len(df)-1, "XRknee1"],
                                            df.at[len(df)-1, "YRknee1"])
def distHipWrist(df):
    
    df.at[len(df)-1, "DistLHipLWrist1"] = distance(df.at[len(df)-1, "XLhip1"],
                                            df.at[len(df)-1, "YLhip1"],
                                            df.at[len(df)-1, "XLwrist2"],
                                            df.at[len(df)-1, "YLwrist2"])
    
    df.at[len(df)-1, "DistLHipRWrist1"] = distance(df.at[len(df)-1, "XLhip1"],
                                            df.at[len(df)-1, "YLhip1"],
                                            df.at[len(df)-1, "XRwrist2"],
                                            df.at[len(df)-1, "YRwrist2"])
    
    
    
    
    
    
    df.at[len(df)-1, "DistRHipLWrist1"] = distance(df.at[len(df)-1, "XRhip1"],
                                            df.at[len(df)-1, "YRhip1"],
                                            df.at[len(df)-1, "XLwrist2"],
                                            df.at[len(df)-1, "YLwrist2"])
    
    df.at[len(df)-1, "DistRHipRWrist1"] = distance(df.at[len(df)-1, "XRhip1"],
                                            df.at[len(df)-1, "YRhip1"],
                                            df.at[len(df)-1, "XRwrist2"],
                                            df.at[len(df)-1, "YRwrist2"])
    
    
    
    
    
    
    df.at[len(df)-1, "DistLHipLWrist2"] = distance(df.at[len(df)-1, "XLhip2"],
                                            df.at[len(df)-1, "YLhip2"],
                                            df.at[len(df)-1, "XLwrist1"],
                                            df.at[len(df)-1, "YLwrist1"])
    
    df.at[len(df)-1, "DistLHipRWrist2"] = distance(df.at[len(df)-1, "XLhip2"],
                                            df.at[len(df)-1, "YLhip2"],
                                            df.at[len(df)-1, "XRwrist1"],
                                            df.at[len(df)-1, "YRwrist1"])
    
    
    
    
    
    
    df.at[len(df)-1, "DistRHipLWrist2"] = distance(df.at[len(df)-1, "XRhip2"],
                                            df.at[len(df)-1, "YRhip2"],
                                            df.at[len(df)-1, "XLwrist1"],
                                            df.at[len(df)-1, "YLwrist1"])
    
    df.at[len(df)-1, "DistRHipRWrist2"] = distance(df.at[len(df)-1, "XRhip2"],
                                            df.at[len(df)-1, "YRhip2"],
                                            df.at[len(df)-1, "XRwrist1"],
                                            df.at[len(df)-1, "YRwrist1"])
    
    
    
def distHipKnee(df):
    
    df.at[len(df)-1, "DistLHipLKnee1"] = distance(df.at[len(df)-1, "XLhip1"],
                                            df.at[len(df)-1, "YLhip1"],
                                            df.at[len(df)-1, "XLknee2"],
                                            df.at[len(df)-1, "YLknee2"])
        
    df.at[len(df)-1, "DistLHipRKnee1"] = distance(df.at[len(df)-1, "XLhip1"],
                                            df.at[len(df)-1, "YLhip1"],
                                            df.at[len(df)-1, "XRknee2"],
                                            df.at[len(df)-1, "YRknee2"])
    
    df.at[len(df)-1, "DistRHipLKnee1"] = distance(df.at[len(df)-1, "XRhip1"],
                                            df.at[len(df)-1, "YRhip1"],
                                            df.at[len(df)-1, "XLknee2"],
                                            df.at[len(df)-1, "YLknee2"])
    
    df.at[len(df)-1, "DistRHipRKnee1"] = distance(df.at[len(df)-1, "XRhip1"],
                                            df.at[len(df)-1, "YRhip1"],
                                            df.at[len(df)-1, "XRknee2"],
                                            df.at[len(df)-1, "YRknee2"])
    
    
    df.at[len(df)-1, "DistLHipLKnee2"] = distance(df.at[len(df)-1, "XLhip2"],
                                            df.at[len(df)-1, "YLhip2"],
                                            df.at[len(df)-1, "XLknee1"],
                                            df.at[len(df)-1, "YLknee1"])
        
    df.at[len(df)-1, "DistLHipRKnee2"] = distance(df.at[len(df)-1, "XLhip2"],
                                            df.at[len(df)-1, "YLhip2"],
                                            df.at[len(df)-1, "XRknee1"],
                                            df.at[len(df)-1, "YRknee1"])
    
    df.at[len(df)-1, "DistRHipLKnee2"] = distance(df.at[len(df)-1, "XRhip2"],
                                            df.at[len(df)-1, "YRhip2"],
                                            df.at[len(df)-1, "XLknee1"],
                                            df.at[len(df)-1, "YLknee1"])
    
    df.at[len(df)-1, "DistRHipRKnee2"] = distance(df.at[len(df)-1, "XRhip2"],
                                            df.at[len(df)-1, "YRhip2"],
                                            df.at[len(df)-1, "XRknee1"],
                                            df.at[len(df)-1, "YRknee1"])


    
def calculateDistances(df):
    distNeckHip(df)
    distNoseWrist(df)
    distHipWrist(df)
    distHipKnee(df)
    distNoseKnee(df)
