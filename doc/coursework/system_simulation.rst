Coursework 1 (2020)
===================

System Simulation
-----------------

In this coursework, you will provide a single report, containing
an overview of an image-guided surgery system of your choice.

The marking scheme is below. Feel free to use any of the jupyter
notebooks used in class, or indeed your own code, in any language.

+------------+-------+-----------------------------------------------------------------------------------------------------------+
| Section    | Marks | Task                                                                                                      |
+============+=======+===========================================================================================================+
| 1          | 0     | Identify an image-guided surgery system in the research literature.                                       |
|            |       |   - Discuss suitability with Module Lead.                                                                 |
+------------+-------+-----------------------------------------------------------------------------------------------------------+
| 2          | 5     | Describe the clinical procedure.                                                                          |
|            |       |   - What is the clinical challenge?                                                                       |
|            |       |   - What is main idea of the engineering solution?                                                        |
|            |       |   - Are there alternatives?                                                                               |
+------------+-------+-----------------------------------------------------------------------------------------------------------+
| 3          | 5     | Identify the imaging types used.                                                                          |
|            |       |   - When are they taken?                                                                                  |
|            |       |   - What is the spatial resolution of each image type?                                                    |
|            |       |   - What is the contrast mechanism being imaged?                                                          |
|            |       |   - What errors would you expect purely from imaging?                                                     |
+------------+-------+-----------------------------------------------------------------------------------------------------------+
| 4          | 5     | Produce a diagram of all coordinate systems                                                               |
|            |       |   - Name each coordinate system                                                                           |
|            |       |   - Label each coordinate system                                                                          |
|            |       |   - Ensure transformation direction is correct                                                            |
|            |       |   - Indicate which transformations are static versus dynamic                                              |
+------------+-------+-----------------------------------------------------------------------------------------------------------+
| 5          |       | Create a simulation environment to estimate Target Registration Error (TRE)                               |
|            |  - 1  |   - It should use 3D coordinates                                                                          |
|            |  - 1  |   - Produce clear system diagram                                                                          |
|            |  - 2  |   - State assumptions/simplifications                                                                     |
|            |  - 1  |   - State which parameters you are interested in simulating                                               |
|            |  - 4  |   - State what noise model you are using for each parameter and why                                       |
|            |  - 2  |   - State how many spacial locations you are studying. Justify.                                           |
|            |  - 8  |   - Estimate system TRE                                                                                   |
|            |  - 1  |   - Discuss, does your simulation of TRE look reasonable?                                                 |
+------------+-------+-----------------------------------------------------------------------------------------------------------+
| 6          | 5     | Analyse visualisation                                                                                     |
|            |       |   - Describe visualisation method used                                                                    |
|            |       |   - Is visualisation multimodal? If so, is it easy to interpret?                                          |
|            |       |   - Does visualisation show alignment uncertainty?                                                        |
|            |       |   - Is it easy to see when system is wrong? e.g. not tracking?                                            |
|            |       |   - How could visualisation be improved?                                                                  |
+------------+-------+-----------------------------------------------------------------------------------------------------------+
| 7          | 5     | Analyse User Interface                                                                                    |
|            |       |   - Who are the users?                                                                                    |
|            |       |   - What training would they need to use the system?                                                      |
|            |       |   - Are there usability constraints, specific for the OR?                                                 |
|            |       |   - How many steps can you identify?                                                                      |
|            |       |   - How much of an interruption to the normal workflow iw is?                                             |
+------------+-------+-----------------------------------------------------------------------------------------------------------+
| 8          | 5     | Analyse Evaluation Methodology                                                                            |
|            |       |   - Describe how system was evaluated, e.g. accuracy?                                                     |
|            |       |   - Discuss limitations of e.g. phantom, animal study etc?                                                |
|            |       |   - Does evaluation use FLE, FRE, TRE? Is methodology sufficient?                                         |
|            |       |   - How would evaluation transfer to the OR?                                                              |
+------------+-------+-----------------------------------------------------------------------------------------------------------+

