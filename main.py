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

For example, if you buy 8 cans of chick peas, you will pay $1.25 * 6 = $7.50 for the first 6 cans plus  $1.50 * 2 = $3.00 for the remaining 2 cans. So, in total, you will pay $10.50.
Write a function that takes the number of cans as input and calculates the price for that number of cans.

"""

def calculate_price(num_cans):
    return num_cans * 1.0


"""
Exercise 7 (Challenge)
Write a function to return the distance between 2 points on earth.  

Use the link https://www.movable-type.co.uk/scripts/latlong.html for an explanation
of distance calculation, and implement "haversine" code in python

On the same webpage, there is a distance calcuator so you can try out some 
examples to see if your function matches the offical one!

HINT: under the distance section, there is already code for this calculation,
but it is in the Javascript programming language so you cannot directly copy
it here.  For example, to take the sine of an angle in python, you use the 
math.sin(angle) function instead of Math.sin(angle)
"""
def distance( lat1, lon1, lat2, lon2 ):    
    return 0

    

"""
**DO NOT MODIFY BELOW**

Every computer program has what we called a entry point, commonly referred to as "main"
Below is the entry point to the above exercise that creates a webpage so users
can interface with your code
"""

if __name__ == "__main__":
    import gradio as gr

    with gr.Blocks() as demo:
        gr.Markdown("## Grading & Math Utility Exercises")

        gr.Markdown("### Exercise 1: Average Mark")
        gr.Interface(fn=average_mark,
                     inputs=[gr.Number(label="Mark 1"), gr.Number(label="Mark 2")],
                     flagging_mode="never",
                     outputs="number")

        gr.Markdown("### Exercise 2: Convert to Percentage")
        gr.Interface(fn=convert_to_percentage,
                     inputs=[gr.Number(label="Score"), gr.Number(label="Max Score")],
                     flagging_mode="never",
                     outputs="text")

        gr.Markdown("### Exercise 3: Average Percentage of 2 Midterms")
        gr.Interface(fn=calculate_average,
                     inputs=[
                         gr.Number(label="Mark 1"), gr.Number(label="Max 1"),
                         gr.Number(label="Mark 2"), gr.Number(label="Max 2")
                     ],
                     flagging_mode="never",
                     outputs="text")

        gr.Markdown("### Exercise 4: Midterm Weighted (20%)")
        gr.Interface(fn=midterms_weighted,
                     inputs=[
                         gr.Number(label="Mark 1"), gr.Number(label="Max 1"),
                         gr.Number(label="Mark 2"), gr.Number(label="Max 2")
                     ],
                     flagging_mode="never",
                     outputs="text")

        gr.Markdown("### Exercise 5: Cone Surface Area")
        gr.Interface(fn=cone_surface_area,
                     inputs=[gr.Number(label="Radius (r)"), gr.Number(label="Height (h)")],
                     flagging_mode="never",
                     outputs="text")

        gr.Markdown("### Exercise 6: Chick Pea Can Pricing")
        gr.Interface(fn=calculate_price,
                     inputs=[gr.Number(label="Number of Cans")],
                     flagging_mode="never",
                     outputs="text")

        gr.Markdown("### Exercise 7: Haversine Distance")
        gr.Interface(fn=distance,
                     inputs=[
                         gr.Number(label="Latitude 1"), gr.Number(label="Longitude 1"),
                         gr.Number(label="Latitude 2"), gr.Number(label="Longitude 2")
                     ],
                     flagging_mode="never",
                     outputs="text")

    demo.launch()
