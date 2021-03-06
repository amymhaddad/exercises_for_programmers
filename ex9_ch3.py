#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: create constant
GALLONS_PER_SQ_FT = 350

# Step 2: import math
import math

# Step 3: get two inputs from user on length and width of room
ceiling_length = int(input("What is the length of the ceiling? "))

ceiling_width = int(input("What is the width of the ceiling? "))

# Step 4: make calculation to find the area of the ceiling
ceiling_area = ceiling_length * ceiling_width

# Step 5: make calculation to find out how many gallons of paint are needed to paint the ceiling's area
paint_gallons_needed = math.ceil(ceiling_area / GALLONS_PER_SQ_FT)

# Step 6: create statement to show number of gallons of paint needed to paint ceiling
print(f"You'll need {paint_gallons_needed} gallons of paint to paint {ceiling_area} square feet.")
