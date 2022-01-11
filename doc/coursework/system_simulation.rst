Coursework 1 (2022)
===================

Dates
-----

Refer to Moodle.

System Simulation
-----------------

In this coursework, you will provide a single report, containing
an overview of an image-guided interventional system of your choice.

The marking scheme is below. Feel free to use any of the jupyter
notebooks used in class, or indeed your own code, in any language.

Tasks
-----

+------------+-------+---------------------------------------------------------------------------------------------------------------+
| Section    | Marks | Task                                                                                                          |
+============+=======+===============================================================================================================+
| 1          | 0     | Identify an image-guided interventional system in the research literature.                                    |
|            |       |   - Discuss suitability with Module Lead.                                                                     |
+------------+-------+---------------------------------------------------------------------------------------------------------------+
| 2          | 5     | Describe the clinical procedure.                                                                              |
|            |       |   - What is the clinical challenge?                                                                           |
|            |       |   - What is the benefit to the patient?                                                                       |
|            |       |   - What is the benefit to the hospital (or whoever pays for such a device)?                                  |
|            |       |   - What is main idea of the engineering solution?                                                            |
|            |       |   - What is the criteria to determine if the system is a 'success'?                                           |
+------------+-------+---------------------------------------------------------------------------------------------------------------+
| 3          |       | What are the alternatives in the literature?                                                                  |
|            | - 1   |   - Identify alternative approaches                                                                           |
|            | - 2   |   - Discuss at least 2 pro's                                                                                  |
|            | - 2   |   - Discuss at least 2 con's                                                                                  |
+------------+-------+---------------------------------------------------------------------------------------------------------------+
| 4          | 5     | Identify the imaging types used.                                                                              |
|            |       |   - When are they taken?                                                                                      |
|            |       |   - What is the spatial resolution of each image type?                                                        |
|            |       |   - What is the contrast mechanism being imaged?                                                              |
|            |       |   - What errors would you expect from the timeliness of the imaging?                                          |
|            |       |   - Given the clinical procedure, what spatial (geometrical) errors would you expect in the imaging?          |
+------------+-------+---------------------------------------------------------------------------------------------------------------+
| 5          | 5     | Produce a diagram of all coordinate systems                                                                   |
|            |       |   - Name each coordinate system                                                                               |
|            |       |   - Label each coordinate system                                                                              |
|            |       |   - Ensure transformation direction is correct                                                                |
|            |       |   - Indicate which transformations are static versus dynamic                                                  |
|            |       |   - Indicate which transforms are rigid/affine/non-linear                                                     |
+------------+-------+---------------------------------------------------------------------------------------------------------------+
| 6          |       | Create a simulation environment to estimate Target Registration Error (TRE)                                   |
|            |  - 1  |   - It should use 3D coordinates, but if you simplify to some 2D mock example, you lose this point.           |
|            |  - 1  |   - Determine which coordinate system the data will be visualised in, and justify why.                        |
|            |  - 2  |   - State assumptions/simplifications. For example you may just assume certain things are rigid.              |
|            |  - 1  |   - State which parameters you are interested in simulating, or understanding.                                |
|            |  - 4  |   - State what model or statistical distribution you are using for to simulate each parameter and why.        |
|            |  - 2  |   - State how many spacial locations you are studying. This might be 1 point in a measurement volume or many. |
|            |  - 8  |   - Estimate system TRE                                                                                       |
|            |  - 1  |   - Discuss, does your simulation of TRE look reasonable?                                                     |
+------------+-------+---------------------------------------------------------------------------------------------------------------+
| 7          | 5     | Analyse visualisation                                                                                         |
|            |       |   - Describe visualisation method used                                                                        |
|            |       |   - Is visualisation multimodal? If so, is it easy to interpret?                                              |
|            |       |   - Does visualisation show alignment uncertainty?                                                            |
|            |       |   - Is it easy to see when system is wrong? e.g. not tracking?                                                |
|            |       |   - How could visualisation be improved?                                                                      |
+------------+-------+---------------------------------------------------------------------------------------------------------------+
| 8          | 5     | Analyse User Interface                                                                                        |
|            |       |   - Who are the users?                                                                                        |
|            |       |   - What training would they need to use the system?                                                          |
|            |       |   - Are there usability constraints, specific for the OR?                                                     |
|            |       |   - How many steps in the workflow can you identify?                                                          |
|            |       |   - How much of an interruption to the normal workflow iw is?                                                 |
+------------+-------+---------------------------------------------------------------------------------------------------------------+
| 9          |       | Analyse Evaluation Methodology                                                                                |
|            | - 2   |   - Describe how system was evaluated, e.g. accuracy?                                                         |
|            | - 1   |   - Discuss limitations of e.g. phantom, animal study etc?                                                    |
|            | - 1   |   - Does evaluation use FLE, FRE, TRE? Is methodology sufficient?                                             |
|            | - 1   |   - How would evaluation transfer to the OR?                                                                  |
+------------+-------+---------------------------------------------------------------------------------------------------------------+
| 10         |       | Can the system be made into a product?                                                                        |
|            | - 3   |   - Do a brief citation search. How has the research progressed since this paper?                             |
|            | - 2   |   - If the system has become a commercial product, identify a vendor, and comment on their claims.            |
|            | - 0   |   - OR                                                                                                        |
|            | - 2   |   - Comment upon what would be the reasonable next steps achieve a minimum viable product.                    |
+------------+-------+---------------------------------------------------------------------------------------------------------------+

