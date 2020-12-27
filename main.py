import cv2
if __name__ == "__main__":
    cam=cv2.VideoCapture(0)
    time=0
    background=cam.read()[1]
    while True:
        image=cam.read()[1]
        text=''
        if time<50:
            text='Taking Background Image Plz get aside'
            cv2.putText(image,text,(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
        elif 120>time:
            cv2.putText(image,str(3-(time-50)//30),(200,200),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0),5)
        else:
            
            cv2.destroyAllWindows()
            break
        cv2.imshow('image',image)
        if cv2.waitKey(70)==ord('q'):
            cv2.destroyAllWindows()
            break
        time+=1
    time=0
    image=cam.read()[1]
    while True:
        image=cam.read()[1]
        text=''
        if time<100:
            text='Taking Cloak Image'
            cv2.putText(image,text,(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
            text='Make sure cloak cover whole screen'
            cv2.putText(image,text,(1,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
        elif 120>time:
            cv2.putText(image,str(3-(time-50)//30),(200,200),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0),5)
        else:
            
            cv2.destroyAllWindows()
            break
        cv2.imshow('image',image)
        if cv2.waitKey(70)==ord('q'):
            cv2.destroyAllWindows()
            break
        time+=1
    min_r=float('inf')
    min_g=float('inf')
    min_b=float('inf')
    max_r=float('-inf')
    max_g=float('-inf')
    max_b=float('-inf')
    for i in range(image.shape[0]):
        for j in range(image.shape[0]):
            if min_r>image[i][j][0]:
                min_r=image[i][j][0]
            if max_r<image[i][j][0]:
                max_r=image[i][j][0]
            
            if min_g>image[i][j][1]:
                min_g=image[i][j][1]
            if max_g<image[i][j][1]:
                max_g=image[i][j][1]
            
            if min_b>image[i][j][2]:
                min_b=image[i][j][2]
            if max_b<image[i][j][2]:
                max_b=image[i][j][2]
    print(max_b,max_g,max_r)
    while True:
        image=cam.read()[1]
        
        cv2.imshow('image',image)
        if cv2.waitKey(70)==ord('q'):
            cv2.destroyAllWindows()
            break



        
    cam.release()
    
    