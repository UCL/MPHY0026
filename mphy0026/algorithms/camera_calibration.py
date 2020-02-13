#Python functions to support MedPhys Taught Module workshop on calibration and tracking

import numpy as np
import csv 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def load_intrinsic(filein):
    """
    loads a text file formatted, consisting of a 3x3 
    projection project matrix, followed by a row of 
    distortion coefficients.
    :return: intrinsic, distortion
    """
    projection=np.zeros((1,3))
    distortion=np.zeros((1,5))
    with open(filein,'rt') as csvfile:
        reader = csv.reader(filter(lambda row: row[0]!='#',csvfile),delimiter=" ")
        rownumber=1
        for row in reader:
            #some files have blanks at the end of each line
            length=len (row)
            if ( rownumber < 4 ):
                while ( len(row) > 3 ):
                    row.pop()
            else:
                while ( len(row) > 5 ):
                    row.pop()

            n=np.array([float (col) for col in row])
            if (rownumber == 1):
                projection=n
            else:
                if ( rownumber < 4 ):
                    projection=np.concatenate((projection,n),axis=0)
                else:
                    distortion=n
            rownumber += 1

    projection = np.reshape(projection,(3,3))
    distortion = np.reshape(distortion, (1,5))

    return (projection, distortion)

def load_model_points(filein, offset = np.zeros((1,4))):
    """
    loads a four column text file
    :params: filename, optional offset, which is subtracted from 
    each row
    :return: array of points
    """
    m=np.zeros((4))
    with open(filein,'rt') as csvfile:
        reader = csv.reader(filter(lambda row: row[0]!='#',csvfile),delimiter=" ")
        rownumber=1
        for row in reader:
            n=np.array([float (col) for col in row])
            if ( n.shape[0] == offset.shape[0]):
                n=np.subtract(n , offset)
            if (rownumber == 1):
                m=n
            else:
                m=np.concatenate((m,n),axis=0)
            rownumber += 1

    cols=int(m.shape[0]/(rownumber -1 ))

    m = np.reshape ( m , (rownumber -1, cols) )
    return m

def load_4x4_Matrix(filein):
    m=np.zeros((1,4))
    with open(filein,'rt') as csvfile:
        reader = csv.reader(filter(lambda row: row[0]!='#',csvfile),delimiter=" " , skipinitialspace=True)
        rownumber=1
        for row in reader:
            #some files have blanks at the end of each line
            while ( len(row) > 4 ):
                row.pop()

            n=np.array([float (col) for col in row])
            if (rownumber == 1):
                m=n
            else:
                m=np.concatenate((m,n),axis=0)
            rownumber += 1

    cols=int(m.shape[0]/(rownumber -1 ))

    m = np.reshape ( m , (rownumber -1, cols) )
    return m

def multiply_points_by_4x4 ( pointsin, matrix ):
    #points in is 4 columns, 1st column is point id
    m=pointsin[:,1:4]
    rows=m.shape[0]
    ids=np.reshape(pointsin[:,0],(rows,1))
    ones=np.reshape(np.ones(rows),(rows,1))
    m=np.transpose(np.concatenate((m,ones),axis=1))

    m=np.transpose(np.matmul(matrix,m))
    m=m[:,0:3]
    m=np.concatenate((ids,m),axis=1)
    return m

def project ( lens3D, intrinsic ):
    #does the projection from 3D points relative to the lens to screen points
    m=lens3D[:,1:4]
    rows=m.shape[0]
    ids=np.reshape(lens3D[:,0],(rows,1))

    m=np.transpose(m)
    m=np.divide(m,m[2,:])
    m=np.transpose(np.matmul(intrinsic,m))
    m=m[:,0:2]
    m=np.concatenate((ids,m),axis=1)

    return m
def distort ( lens3D, d ):
    
    m=lens3D[:,1:4]
    rows=m.shape[0]
    ids=np.reshape(lens3D[:,0],(rows,1))
    m=np.transpose(m)
    m=np.divide(m,m[2,:])

    r=np.linalg.norm(m[0:2,:],axis=0)
    for row in range(0,rows):
        rfactor=1 + d[0,0] * r[row]**2 + d[0,1] * r[row]**4 + d[0,4] * r[row]**6
        rdpixels=np.multiply(m[0:2,row],rfactor)

        twoponexy=m[0,row] * m[1,row] * 2 * d[0,2]
        twoptwoxy=m[0,row] * m[1,row] * 2 * d[0,3]
        xfactor=twoponexy + d[0,3]* ( r[row]**2 + 2* m[0,row]**2)
        yfactor=twoptwoxy + d[0,2]* ( r[row]**2 + 2* m[1,row]**2)
        
        tdrdpixels = rdpixels + ([xfactor,yfactor])
        #if ( row % 50 == 00 ):
        #    print ("For row = " , row, m[0:2,row], "becomes",  rdpixels, "becomes", tdrdpixels)
        
        m[0:2,row]=tdrdpixels
        #if ( row == 0):
        #    pixout=rdpixels
        #else:
        #    pixout=np.concatenate((pixout,rdpixels),axis=0)
   
    m=np.transpose(m)
    m=np.concatenate((ids,m),axis=1)

    return m 

def calculate_errors ( screenPoints , projectedPoints ):
    screenRows=screenPoints.shape[0]
    projectedRows=projectedPoints.shape[0]
    deltas=np.zeros((screenRows,2))
    count = 0
    for srow in range (0,screenRows):
        id=screenPoints[srow,0]
        count += 1
        #this will be slow, but should be OK for our purposes
        for prow in range ( 0, projectedRows):
            if ( id == projectedPoints[prow,0]):
                deltas[srow,:] = np.subtract( screenPoints[srow,1:3] , projectedPoints[prow,1:3])
                break
            if ( prow == projectedRows - 1 ):
                print ( "NO MATCH for " , id )


    return deltas

def plot_errors ( imageFileName, projectedPoints, screenPoints , cropToImage = True ):
    img=mpimg.imread(imageFileName)
    fig,ax1 = plt.subplots(figsize=(12,8))
    ax1.imshow(img)
    if cropToImage:
        ax1.set_ylim([0,img.shape[0]])
        ax1.set_xlim([0,img.shape[1]])
    ax1.scatter(projectedPoints[:,1],projectedPoints[:,2])
    ax1.scatter(screenPoints[:,1],screenPoints[:,2])
    
    return






