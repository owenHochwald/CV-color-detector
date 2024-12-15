import cv2
from PIL import Image

from util import get_limits


color_map = {
    "yellow": [0, 255, 255],
    "red": [0, 0, 255],
    "green": [0, 255, 0],
    "blue": [255, 0, 0]
}


def main():
    print("Select a color to detect:")
    print("1. Yellow")
    print("2. Red")
    print("3. Green")
    print("4. Blue")
    
    color = None

    while True:
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            color = color_map["yellow"]
            break
        elif choice == "2":
            color = color_map["red"]
            break
        elif choice == "3":
            color = color_map["green"]
            break
        elif choice == "4":
            color = color_map["blue"]
            break
        else:
            print("Invalid input. Please try again.")
            
    cap = cv2.VideoCapture(0)


    while True:
        ret, frame = cap.read()  # Read a frame from the webcam
        
        # Convert to HSV
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # TODO: create a color mask for a range of colors that can be requested by the user to select for different colors

        lowerLimit, upperLimit = get_limits(color=color)
        

        # location of all pixels of the color range requested
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        
        # convert the mask to an image
        mask_ = Image.fromarray(mask)
        
        # get the boundary box
        bbox = mask_.getbbox()
        
    # get the boundary box
        bbox = mask_.getbbox()
        if bbox is not None:
            x1, y1, x2, y2 = bbox

            # Draw rectangle around the object
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)

            # Add text to the boundary box
            # Add text to the boundary box
            cv2.putText(frame, f"{list(color_map.keys())[list(color_map.values()).index(color)]} object detected", (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)                
        cv2.imshow('frame', frame)  # Display the current frame in a window named 'frame'
        
        # Check if the 'q' key is pressed to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()