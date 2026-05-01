import math

"""
Exercise 1
Let's create a function to calculate the average grade for 2 midterms. 
Assume that the maximum score on each is 100 points. 
Write a function averageMark that takes the grades a student achieved on the midterms 
(out of 100) and calculates their average.
"""
def average_mark(mark1, mark2):
    return mark1 + mark2

"""
Exercise 2
It is not likely that the maximum number of points on a midterm is going to be 100. Write a function convert_to_percentage that takes your score and the maximum score on the test as input and returns the percentage you scored on the test.

NOTE: what happens when the max points is not valid?  
"""
def convert_to_percentage(mark, max_points):
    return 0 

"""
Exercise 3
Write a function calculateAverage that takes 4 inputs (two actual test scores and two maximum possible test scores) and returns the average percentage you achieved on the midterms. 

Also try to write it using multiple lines.  I have created a couple of variables for you to get you started.
Replace all the 0s with appropriate code
"""
def calculate_average(mark1, max1, mark2, max2):
    score1_percentage = 0
    score2_percentage = 0
    return 0
    
"""
Exercise 4
Finally, each midterm is worth 10% of your final grade. Write a function  that takes 4 inputs (two actual test scores and two maximum possible test scores) and returns the percentage (max being 20%) that the midterms will contribute towards your final grade. Test your function
"""
def midterms_weighted(mark1, max1, mark2, max2):
    return 0

"""
Exercise 5
Write a function that takes the height and the radius of a base of a right cone as 
input and returns its surface area.  The formula for the surface area is
   A = PI*r(r + sqrt(h^2+r^2))
"""
def cone_surface_area(r, h):
    return 0

"""
Exercise 6
A local supermarket has a promotion that if you buy cans of chick peas in multiples of 3 you pay $1.25 per can. For the number of cans that are above a multiple of 3, you are charged $1.50 per can.
"""
def calculate_price(num_cans):
    return num_cans * 1.0

"""
Exercise 7 (Challenge)
Write a function to return the distance between 2 points on earth.  
"""
def distance(lat1, lon1, lat2, lon2):    
    return 0

"""
**DO NOT MODIFY BELOW**

Every computer program has what we called a user interface.
Below is a much more complex user interface than what the textbook provides.
You run the following command in the terminal to start this program:

python main.py
"""

def gui():
    try:
        import gradio as gr
    except ImportError:
        print("\n[Error] Gradio not found. Please use the CLI or run 'pip install gradio'.")
        return

    with gr.Blocks() as demo:
        gr.Markdown("## Grading & Math Utility Exercises")
        
        # Exercise interfaces
        gr.Interface(fn=average_mark, inputs=[gr.Number(label="Mark 1"), gr.Number(label="Mark 2")], outputs="number", title="Ex 1: Average Mark", flagging_mode="never")
        gr.Interface(fn=convert_to_percentage, inputs=[gr.Number(label="Score"), gr.Number(label="Max Score")], outputs="text", title="Ex 2: Percentage", flagging_mode="never")
        gr.Interface(fn=calculate_average, inputs=[gr.Number(label="Mark 1"), gr.Number(label="Max 1"), gr.Number(label="Mark 2"), gr.Number(label="Max 2")], outputs="text", title="Ex 3: Avg Percentage", flagging_mode="never")
        gr.Interface(fn=midterms_weighted, inputs=[gr.Number(label="Mark 1"), gr.Number(label="Max 1"), gr.Number(label="Mark 2"), gr.Number(label="Max 2")], outputs="text", title="Ex 4: Weighted Grade", flagging_mode="never")
        gr.Interface(fn=cone_surface_area, inputs=[gr.Number(label="Radius"), gr.Number(label="Height")], outputs="text", title="Ex 5: Cone Surface Area", flagging_mode="never")
        gr.Interface(fn=calculate_price, inputs=[gr.Number(label="Cans")], outputs="text", title="Ex 6: Chick Pea Pricing", flagging_mode="never")
        gr.Interface(fn=distance, inputs=[gr.Number(label="Lat 1"), gr.Number(label="Lon 1"), gr.Number(label="Lat 2"), gr.Number(label="Lon 2")], outputs="text", title="Ex 7: Haversine Distance", flagging_mode="never")

    demo.launch()

def cli():
    while True:
        print("\n--- Exercise Menu ---")
        print("1. Average Mark\n2. Percentage\n3. Avg Percentage\n4. Weighted Grade\n5. Cone Area\n6. Chick Peas\n7. Distance")
        print("G. Start GUI (Gradio)\nQ. Quit")
        
        choice = input("\nSelection: ").strip().upper()
        if choice == 'Q': break
        if choice == 'G': gui(); break
        
        try:
            if choice == '1':
                print(f"Result: {average_mark(float(input('M1: ')), float(input('M2: ')))}")
            elif choice == '2':
                print(f"Result: {convert_to_percentage(float(input('Score: ')), float(input('Max: ')))}")
            elif choice == '3':
                print(f"Result: {calculate_average(float(input('M1: ')), float(input('Mx1: ')), float(input('M2: ')), float(input('Mx2: ')))}")
            elif choice == '4':
                print(f"Result: {midterms_weighted(float(input('M1: ')), float(input('Mx1: ')), float(input('M2: ')), float(input('Mx2: ')))}")
            elif choice == '5':
                print(f"Result: {cone_surface_area(float(input('R: ')), float(input('H: ')))}")
            elif choice == '6':
                print(f"Result: ${calculate_price(int(input('Cans: '))):.2f}")
            elif choice == '7':
                print(f"Result: {distance(float(input('Lat1: ')), float(input('Lon1: ')), float(input('Lat2: ')), float(input('Lon2: ')))}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    cli()
