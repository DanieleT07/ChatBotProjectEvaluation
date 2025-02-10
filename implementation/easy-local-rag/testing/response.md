
---
---
# Question How do I align the bands?
Response: Unfortunately, there doesn't seem to be a specific instruction on how to align the bands in your provided context. However, I can provide some general guidance based on the information given.

It appears that you are working with a machine manufactured by Boatopack srl, and you're trying to align the bands (which I assume refer to the wrapping material or sachets).

1. If you're looking for guidance on how to align the wrapping material, you should check if there's any specific setting in the packing page (Screen 19 - Packing page). There might be a setting like "AUTO SAMPLING" or "MANUAL SAMPLING" that can help you adjust the alignment of the bands.
2. If you're having issues with the deviator not functioning correctly, you may want to check the settings under DEVIATOR ON LINE CYCLES, DEVIATOR OFF LINE PHASE, INTERVAL, N° OF SAMPLING, and ACTUAL DATA COUNTER. These settings might be affecting the alignment of the bands.
3. If you're having trouble with the path adjustment rollers (), it's possible that they need to be adjusted independently for both front and rear sides of the wrapping material. Please refer to Fig. 16 - Path adjustment rollers for guidance on how to adjust these.

Please feel free to provide more context or details about your issue, and I'll do my best to help you resolve it!

---
---
# Question How do I adjust the dosing phase?
Response: To adjust the dosing phase, you can follow these steps:

1. Go to the Packing page (Screen 19) and select "SET DATA DEVIATOR ON LINE CYCLES" and enter a value for the number of cycles to count before switching the deviator on line after the doser has started to work.
2. Set the "DEVIATOR ON LINE PHASE" (in millimeters) that specifies when the deviator should turn on.
3. Repeat the process for "DEVIATOR OFF LINE CYCLES" and "DEVIATOR OFF LINE PHASE" to adjust the off-line phase.

Note: The dosing phase is not mentioned in this specific section, but it might be related to the "SET DATA DEVIATOR" option.

---
---
# Question How do I adjust the transverse cut?
Response: To adjust the transverse cut, follow these steps:

1. Make sure the packaging machine is stopped.
2. Access the "Mark page" by navigating through the menu or selecting it from the main screen.
3. Ensure the "Average mode" is disabled (unless you have a specific film type that requires this setting).
4. Set the desired mark phase detection value in the "Set data mark phase detection" field. This value refers to the position of the jaws when the mark is detected, measured in millimeters.
5. Adjust the "Wait cycles" and "Reject cycles" settings as needed to fine-tune the joint detection process. These values control how many machine cycles wait after detecting a joint and how long the doser remains disabled during this time.
6. If you have reels 2 or 3, configure the additional unwinder wait setting as required.
7. Start the packaging machine, ensuring it is properly stabilized before making any further adjustments.

The key to adjusting the transverse cut is to center the mark on the sachet while controlling the film speed. The machine will automatically make small corrections at each cycle if needed. If the error persists, the control may modify the bag length to achieve a stable state. Monitor the "Actual mark position error" field and adjust the phase value if necessary to position the mark as desired.

Please note that any adjustments to the transverse cut should be made when the machine is stopped to avoid disrupting the packaging process or causing errors.

---
---
# Question How do I adjust the vertical cut?
Response: To adjust the vertical cut:

1. Check the manual commands: Ensure that the manual commands are disabled before making any adjustments.
2. Adjust the cam position: Locate the cam with its proximity sensor and put it in the position shown in Fig. 35.

Please note that the adjustment process may require caution as it involves precise movements to ensure proper functioning and safety of the machine.

---
---
# Question How do I align the feeding tubes?
Response: Based on the provided context, it appears that there are multiple sections related to aligning feeding tubes. Here's what I've found:

1. Infeed settings: The infeed page (type 2 optional) has several buttons and settings, including INFEED ENABLE, INFEED HOMING, EMPTYING, HOPPER 1 BOX/HOPPER 3 BOXES, BACK, SET DATA INFEED HOMING OFFSET, INFEED BELT SPEED, INFEED ACCELERATION, and INFEED DECELERATION. You can adjust these settings to align the feeding tubes.
2. Feeding tube alignment: There is no specific mention of "feeding tubes" in the provided context. However, the term "infeed" might refer to the process of feeding material into the machine. If you're looking for information on how to align a specific type of feeding tube, you may need to provide more details or context.
3. Moving the machine: The section 3.1.4 Moving the machine provides instructions on how to lift and move the machine using a fork-lift truck. This might be relevant if you're setting up the machine for use.

To clarify, do you have any specific Questions about aligning feeding tubes or would you like me to summarize any of these sections?

---
---
# Question What should I do in case of leaks?
Response: # Dealing with Leaks
## A113 - AIR LOW PRESSURE: Compressed Air is Down

In case of leaks, follow these steps to address the issue:

1. Check if the FRL valve is opened and adjust it accordingly.
2. Verify the manometer on the air entrance indicates a pressure of 6 bars.

Remember to handle the machine safely and efficiently during installation, as described in Chapter 3.1.1: Warnings for the Installer.

---
---
# Question How do I adjust the brand photocell?
Response: To adjust the brand photocell, you'll need to follow these general steps:

1. **Reel Centering**: Ensure proper tension and alignment on the reels, as mentioned in Section 4.1.3 Reel Centering. If the unwinder group has reached its allowed range (A169 - REEL CENTERING LIMIT REACHED), manually adjust the automatic reel centring system.
2. **Photocell Adjustment**: Locate the photocell sensors that detect the joint or mark on the film. You may need to refer to the specific documentation provided with your brand's equipment for detailed instructions. Some steps are:

a. Find the adjustment screws or dials for each photocell sensor.

b. Consult the user manual or manufacturer's guidelines for the proper adjustment procedures.

c. Adjust the sensors to correctly detect the joint or mark, ensuring accurate reading and tracking (e.g., AVERAGE MODE).

d. Verify the changes by observing the "MARK" LED light; it should turn green once the correct settings are achieved.

If you encounter specific issues with film joints or marks, refer to Section 4.1.3 Mark control:

* **FILM JOINT ENABLE** (optional): Activate or deactivate the film joint function.
* **WAIT CYCLES** (optional): Set the number of cycles to wait from joint detection on the photocell.
* **REJECT CYCLES** (optional): Set the number of cycles to keep the doser disabled while the joint is passing through the feeding area.
* **REJECT DISTANCE** (optional): Set the distance in cycles from the doser to the deviator.

Remember to consult your brand's specific documentation and guidelines for detailed procedures.

---
---
# Question How do I align the bands on the sealing rollers?
Response: ## Aligning Bands on Sealing Rollers

### Context: 4.1.7 Sealing rollers

To align the bands on the sealing rollers, ensure that the pressure is properly adjusted. According to Chapter 4.1.7, "ADJUSTMENT The pressure of the rollers is effected by two springs which load the right axle. The pressure is adjustable by operating on the screw M10 [Fig. 24]."

Before adjusting the pressure, make sure to follow all safety precautions and guidelines provided in the manual.

---
---
# Question How do I adjust the knife to cut correctly?
Response: # Adjusting the Knife to Cut Correctly
## Context: 5.3.26 Knife page

To adjust the knife to cut correctly, you need to calibrate the phase value of the knife cutting. You can do this by entering a value in the "SET DATA PHASE" box on the operator panel. This value adjusts the position of the cut on the empty sachet.

When adjusting the knife, make sure to follow the specific procedures with high precision to ensure correct functioning of the machine. Additionally, ensure that you are working safely and following all safety precautions outlined in the manual, such as wearing suitable clothes, safety footwear, and protective gloves.

Remember to refer to the relevant sections of this manual for more information on adjusting the knife settings and homing the knives.

---
---
# Question How do I set the machine's zero point?
Response: I understand that you're looking to set the machine's zero point.

Based on the provided context, particularly Section 5.3, it seems that there are specific settings for different components of your automatic packaging machine. To set the machine's zero point, I would recommend the following steps:

1. Access the "Heaters Page" (Section 16 in the context).
2. On this page, you will find the "TUBE HEATERS (OPTIONAL)" or "JAWS SET" buttons.
3. Click on the desired button to access the temperature settings for either the tubes/jaws or rolls.
4. Enter the desired temperature value inside the white boxes using the numeric keypad.
5. You should be able to adjust the temperatures of the different components, such as the left and right jaw sets, as well as the rolls.

Please keep in mind that you may need to consult the user manual or training documentation provided by your equipment manufacturer for a more detailed explanation on how to set the machine's zero point, as these steps might vary depending on your specific machine model.

---
---
# Question How do I adjust the pressure of rollers and jaws?
Response: The instructions do not explicitly state how to adjust the pressure of the rollers and jaws, but they provide some general guidance.

For the sealing rollers:

* The pressure of the rollers is adjustable by operating on the screw M10 (Fig. 24).
* The screw loads the right axle, and adjusting it affects the pressure of the rollers.

For the sealing jaws:

* The pressure of the jaws is also adjusted using two springs that load the right axle.
* Adjusting the screws located on the back of the jaws can be used to adjust the pressure.

As with any adjustment process, it is crucial to follow these steps carefully and in the correct order to avoid affecting other components or causing malfunctions. It is recommended consulting the operator manual for specific instructions on adjusting the rollers and jaws.

Additionally, some parameters related to the unwinder reel require adjustments from the operator panel (see details on operator panel instructions). These include:

* Diameter probe adjustment
* End of reel adjustment
* Reel centering adjustment

These adjustments can be found in the packaging material reel section (Figs. 37-38) and may involve setting the position of various sensors or calibrating certain components.

Remember to always follow proper safety procedures when performing any adjustments, as some adjustments may require accessing dangerous parts or situations. If you are unsure about how to perform an adjustment or need further clarification, consult with a qualified technician or the machine's manufacturer.

---
---
# Question How do I replace the bearings of rollers and jaws?
Response: # Replacing Bearings of Rollers and Jaws: Procedure Overview
## Chapter 4.1.7: Sealing Rollers
To replace the bearings of rollers and jaws, please follow these steps:

* Ensure that you have put on suitable clothes, safety footwear, protective gloves, and eyewear.
* Switch off and disconnect the power supply to the machine.
* Remove any protective covers or shields from the area you will be working in.
* Locate the bearing housings and gently loosen any screws or bolts holding them in place.

---
---
# Question How do I change the reel?
Response: To change the reel on this machine, you would need to follow these steps:

**Reel Centering**

* Access the operator panel (Panel PC) and navigate to the "Reel Centering" button in the bottom left bar.
* Press the "Reel Centering" button to enable or disable the automatic centering of the coil on the machine.

**Moving Reels**

* Use the "Reel Right Arrow" and "Reel Left Arrow" buttons (in the bottom left bar) to move the reel position.
	+ The direction of movement is defined by the frontal view of the machine.

**Tips**

* Make sure you correctly set up the parameters, such as reel diameter, before changing reels.
* Check the operator manual or online documentation for specific instructions on reel changing procedures and any safety precautions that may be necessary.

If you have reached the end of the film reel and need to change it:

1. Stop the machine immediately if possible.
2. Follow the specific instructions provided with your machine or consult a technician if necessary.
3. If you are unable to reach the end of the reel, check for any issues with the unwinder (e.g., A166 - END OF FILM REEL BROKEN) before attempting to change the reel.

Please note: These steps may not be exhaustive, and it is recommended that you consult the operator manual or online documentation for specific instructions on changing reels for your machine.

---
---
# Question How do I adjust the film joint photocell?
Response: To adjust the film joint photocell:

1. Go to the "Mark" page (Screen 13).
2. Ensure that the "FILM JOINT ENABLE" button is green and enabled.
3. Adjust the "WAIT CYCLES" value as needed. This variable controls how many machine cycles the system waits after detecting a film joint before enabling the doser again.
4. Adjust the "REJECT CYCLES" value as needed. This variable determines how many cycles the system keeps the doser disabled while the joint is passing through the feeding area.
5. Adjust the "REJECT DISTANCE" value as needed. This variable specifies the number of cycles from the doser to the deviator.
6. Save your adjustments and restart the machine.

Alternatively, if you are experiencing issues with the film joint photocell not detecting joints or incorrectly detecting false marks:

1. Refer to the SICK photocell manual for guidance on maintaining and troubleshooting the photocell.
2. Ensure that the photocell is clean and free of any obstructions that may affect its performance.
3. Check the lens cover on the photocell and ensure it is free of any dirt or debris.
4. Consult with a qualified technician if you are unsure about how to adjust the film joint photocell.

Note: The FILM JOINT ENABLE 2,3 button (optional) allows you to enable the film joint function on reels 2 and 3.

---
---
# Question How do I clean the sealing units?
Response: # Cleaning the Sealing Units

## Cleaning the Sealing Rolls: Chapter 4.1 - Sealing System

To clean the sealing units, refer to Chapter 4.1.7 - Sealing Rollers, where you will find that the peripheral speed of the sealing rollers is equal to the rubbered rollers' speed. To maintain the best possible sealing, a thermocouple keeps the temperature constant.

When cleaning the sealing rolls, make sure not to disrupt their movement or adjust the pressure while the machine is in operation. For adjustments, refer to Chapter 4.1.7 - Sealing Rollers and follow the instructions provided.

Remember to wear suitable clothing, safety footware, and protective gloves when performing maintenance tasks on the packaging machine.

---
---
# Question How can we resolve this alarm? ALARM MOTOR/CUMULATIVE DRIVE PRINTER
Response: # Resolving the Alarm: MOTOR/CUMULATIVE DRIVE PRINTER

## A200: PRINTER MOTOR ALARM
Given that the alarm code falls under the "PRINTER MOTOR ALARM" category (A200), it's likely related to an issue with the motor or drive of the printer. To resolve this, check the drive and refer to the drive manual for the specific alarm code. If necessary, contact BOATO PACK or the local SBC Service for further assistance.

---
---
# Question How can we resolve this alarm? ALARM MOTOR/CUMULATIVE DRIVE JAWS
Response: # Resolving Alarm: Motor/Cumulative Drive Jaws

## Context - A196: JAWS MOTOR ALARM

The alarm indicates that the motor used to move the sealing jaws is operating at an excessive voltage. To resolve this issue, please check the drive and consult the drive manual for the corresponding alarm code. If needed, contact BOATO PACK or the local SBC Service for assistance.

---
---
# Question How can we resolve this alarm? ALARM MOTOR/CUMULATIVE DRIVE FILM
Response: # Resolving the FILM Motor/Cumulative Drive Alarm
## A197 - FILM MOTOR ALARM: The motor utilized to move the sealing FILM is working at too high a voltage.

To resolve this alarm, you should check the drive and refer to its manual for the relevant alarm code. It's essential to ensure that the FILM motor voltage is within the recommended specifications to prevent damage or malfunction. If you need further assistance, contact BOATO PACK or the local SBC Service for guidance.

---
---
# Question How can we resolve this alarm? ALARM MOTOR/CUMULATIVE DRIVE KNIFE
Response: # Resolve the ALARM MOTOR/CUMULATIVE DRIVE KNIFE
## Relevant Context: A198 - KNIFE MOTOR ALARM

The ALARM MOTOR/CUMULATIVE DRIVE KNIFE indicates that there is an issue with the motor or drive of your cut knife. To resolve this alarm, follow the steps outlined in the drive manual for the associated alarm code. Additionally, you may need to contact BOATO PACK or the local PARKER SBC Service for further assistance if required.

---
---
# Question How can we resolve this alarm? ALARM MOTOR/CUMULATIVE DRIVE DOSER
Response: # Resolving ALARM MOTOR/CUMULATIVE DRIVE DOSER

## A207/208, A206, A202, and A201: INFEED MOTOR ALARM & LIQUID DOSER MOTOR ALARM

To resolve this alarm, first check the drive of the liquid doser (or powder doser in case of A201) to determine the cause of the alarm. Refer to the drive manual for specific guidance on addressing the issue. If assistance is needed, contact BOATO PACK or local SBC Service.

Note: Since the error code is not explicitly mentioned, it's unclear which specific drive or motor is causing the alarm. However, following the recommended steps and consulting the relevant manuals should help troubleshoot the issue.

---
---
# Question How can we resolve this alarm? ALARM MOTOR/CUMULATIVE DRIVE STRIP
Response: # Resolving the M/C Drive Strip Alarm
## A199: STRIP MOTOR ALARM - Motor/Cumulative Drive Strip Error

The `ALARM MOTOR/CUMULATIVE DRIVE STRIP` message indicates a problem with the strip knife's motor or drive system. To resolve this alarm, you should:

1. Check the drive system and refer to the drive manual for further guidance on resolving the specific alarm code associated with this error.
2. If necessary, contact BOATO PACK or the local PARKER SBC Service for assistance in troubleshooting and resolving the issue.

Remember to verify that there are no mechanical issues affecting the device before attempting to restore normal operation.

---
---
# Question How can we resolve this alarm? ALARM PRINTER DEVICE NOT READY
Response: # Resolving the ALARM PRINTER DEVICE NOT READY

## A234: PRINTER DEVICE ALARM
To resolve this alarm, first check the printer unit referred to in the printer manual. The problem may be caused by an issue with the printing unit itself. If the problem persists after checking and troubleshooting the printer unit, it is recommended to contact BOATO PACK or the local SBC Service for further assistance.

---
---
# Question How can we resolve this alarm? ALARM PRINTER HOMING TIMEOUT
Response: # Resolving Alarm: PRINTER HOMING TIMEOUT
## A232 - PRINTER HOMING TIMEOUT: The homing movement of the printer has exceed the allowed time. Check the correct running of the motor and the detection sensors.

To resolve this alarm, follow these steps:

* Check the correct running of the motor and the detection sensors for the printer.
* Refer to the drive manual for any specific instructions related to this alarm code (A232).
* If the issue persists, contact BOATO PACK or the local SBC Service for assistance.

---
---
# Question How can we resolve this alarm? ALARM PRINTER OVERTRAVEL
Response: # Resolving Printer Overtravel Alarm: A233

## Context Chapter: A233 - PRINTER OVERTRAVEL
To resolve this alarm, you will need to check the stroke length parameter in the HMI panel. Also, verify the positioning and functioning of the printer overtravel sensor.

Make sure that the printer is not reaching the mechanical limit of its stroke, which would trigger the alarm. If the issue persists, please consult the relevant drive manual or contact BOATO PACK or local SBC Service for further assistance.

---
---
# Question How can we resolve this alarm? ALARM DOSER HOMING TIMEOUT
Response: # Resolving ALARM DOSER HOMING TIMEOUT

## A235: POWDER DOSER HOMING TIME OUT

According to the provided context, the alarm "ALARM DOSER HOMING TIMEOUT" indicates that the homing movement of the powder doser has exceeded the allowed time. To resolve this alarm, please check the correct running of the motor and the detection sensors associated with the powder doser's homing mechanism.

---
---
# Question How can we resolve this alarm? ALARM DOSER MOVEMENT TIMEOUT
Response: # Resolving Doser Movement Timeout Alarm
## A180: Doser Movement Time Out

The doser movement timeout alarm indicates that the doser has not reached its designated position (on line or off line) within the allowed time. To resolve this issue, you need to check the doser movement system and ensure that it is functioning properly.

Check the following:

* Verify if there are any mechanical issues with the doser's movement mechanism.
* Check for any blockages or obstructions in the doser's path that might be preventing it from reaching its target position.
* Ensure that all connections and wiring associated with the doser's movement system are secure and not damaged.

Once you have identified and resolved the issue, restart the machine to see if the alarm is cleared. If the problem persists, refer to the "ALARM PAGES" in your control panel for more information on troubleshooting and possible solutions.

---
---
# Question How can we resolve this alarm? ALARM DOSER OUT OF LINE
Response: # Resolving the DOSER OUT OF LINE Alarm

## Relevant Context: Not specified (Alarm codes not corresponding to provided context)

The DOSER OUT OF LINE alarm requires a check on the doser's setup and configuration. It seems a mechanical issue with the doser itself or its connection may be causing the problem.

To resolve this alarm, ensure that the doser is properly connected and aligned according to the manufacturer's guidelines (if applicable). If the issue persists after checking the doser's setup, it might be necessary to consult the machine's manual for detailed troubleshooting procedures or contact the manufacturer for further assistance.

---
---
# Question How can we resolve this alarm? PSU OVERLOAD ALARM
Response: # Resolving PSU OVERLOAD ALARM

## A133: PSU OVERLOAD ALARM
To resolve this alarm, you need to check related circuit breakers and restore them. Also, inspect the device connected for any mechanical issues that may be causing the overload.

Remember to switch off the machine before performing any maintenance or troubleshooting to ensure your safety.

---
---
# Question How can we resolve this alarm? ETHERCAT NETWORK COMMUNICATION ALARM
Response: # ETHERCAT NETWORK COMMUNICATION ALARM Resolution

## Chapter: 6.1 Troubleshooting, Alarm Type: ETHERCAT NETWORK COMMUNICATION ALARM

The ETHERCAT NETWORK COMMUNICATION ALARM indicates a potential issue with the EtherCat network communication between the machine's control panel and other connected devices. To resolve this alarm:

1. Check the EtherCat network for any connectivity issues or configuration errors.
2. Verify that all devices connected to the EtherCat network are properly configured and communication is functioning correctly.
3. Review the ALARM PAGE on the control panel to identify if there are any specific error messages or codes indicating the root cause of the alarm.
4. Consult the machine's manual or manufacturer's documentation for troubleshooting guidance on resolving EtherCat network communication issues.

Remember, resolving this alarm may require accessing the machine's EtherCat configuration settings, so ensure you have the necessary permissions and knowledge to make changes.

---
---
# Question How can we resolve this alarm? SYSTEM MAJOR ALARMS (GENERIC) - CHECK DIAGNOSTIC
Response: # Resolving SYSTEM MAJOR ALARMS (GENERIC) - CHECK DIAGNOSTIC Alarm

## 6.1 Troubleshooting: TROUBLESHOOTING FOREWORD

---
---
# Question How can we resolve this alarm? SYSTEM MAJOR ALARMS (AXES) - CHECK DIAGNOSTIC
Response: # Resolving SYSTEM MAJOR ALARMS (AXES) - CHECK DIAGNOSTIC Alarm

## 6.1 Troubleshooting: Foreword
To resolve this SYSTEM MAJOR ALARMS (AXES) alarm with the message "CHECK DIAGNOSTIC", you need to check the diagnostic system to identify the root cause of the issue.

Since there is no specific information provided about why the diagnostic system is not functioning properly, I would recommend checking all possible causes listed under A162/163, A135/136, A138, A137, and A154/161 alarm types. This includes checking circuit breakers, inverters for mechanical issues or overload conditions.

Additionally, it might be helpful to check the control panel's ALARM PAGES to see if any specific information is shown about the type of alarm that triggered this message.

---
---
# Question Why machine is not moving in manual mode?
Response: # Why the machine is not moving in manual mode?

## 3.7: Safety System

The machine is designed to move at a low speed when in manual mode, but it will only start moving if all safety guards are in place. If you have removed or bypassed any safety guards, the machine will not move.

Additionally, ensure that the machine is placed on a level surface and has sufficient space around it for easy operation.

---
---
# Question Why machine is not moving after switch on?
Response: # Why machine is not moving after switch on?

## Context: Chapter 3, Installation and Commissioning

The machine may not be moving after switching it on because the line phases have been connected incorrectly. Please check that the line phases are properly connected according to the manual's instructions. Also, ensure that the power supply has been turned off before making any changes, and then restore the power supply once the connections have been corrected.

---
---
# Question Why machine is not moving after switching from manual mode to automatic mode?
Response: # Machine Not Moving After Switching from Manual Mode to Automatic Mode

## 3.6 Positioning of the machine: Operating Instructions
The issue you're experiencing may be due to incorrect setup or configuration of the machine in its definitive position. Ensure that the machine is set up in a perfectly levelled area with sufficient space around it, allowing for easy movement during normal packaging operations.

It's also possible that there might be an error with the power supply phases sequence (A114 - POWER SUPPLY PHASES SWAPPED ALARM). Double-check that the line phases are connected correctly and switch off the machine if necessary. Re-establish correct connections before restarting the machine.

Another potential cause could be related to the doser movement system, as indicated by an error code A180 - DOSER MOVEMENT TIME OUT or A179 - DOSER OUT OF LINE. Verify that the doser is in its proper position and functioning correctly during manual and automatic movements.

For assistance with resolving this issue, please refer to the machine's Instruction Manual or contact our Technical Department for further clarification.

---
---
# Question Doser is enabled and in line, but it does not move, why?
Response: The issue with the Doser not moving could be due to several reasons.

1. **Doser not enabled**: Make sure that the doser is indeed enabled on the Doser selection page (Screen 30). If it's not enabled, the system won't allow the doser to move.

2. **Invalid mode**: Check if the agitator mode is set correctly (AGITATOR MODE button in Agitator page). Ensure that you're not trying to run the agitator when it's disabled, which could prevent any movement.

3. **Doser stuck or faulty**: Sometimes, mechanical issues can cause dosers to malfunction. If the doser is faulty or stuck, it won't move even if enabled. In this case, you might need to troubleshoot or replace the doser as required.

4. **Software/hardware configuration issue**: It's possible that a software or hardware installation/configuration issue may be preventing the doser from moving. Check the error logs and system configurations for any anomalies or inconsistencies that could be causing the problem.

5. **User input incorrect**: Double-check your inputs, especially if there are parameters that need to be adjusted before the doser can move (e.g., speed settings). Ensure that you're entering valid data in areas where it's necessary for the doser to function correctly.

To resolve this issue, I recommend:

1. Inspect the Doser selection page and verify that the doser is enabled.
2. Check the Agitator mode setting and adjust if necessary.
3. Investigate any mechanical issues with the doser (if applicable).
4. Review error logs and system configurations for potential software or hardware-related issues.
5. Verify user input and correct any incorrect data.

If none of these steps resolve the issue, consider consulting a technical support specialist or seeking maintenance assistance to troubleshoot further.

---
---
# Question The sachets are leaking product, how can I fix it?
Response: # Sachet Leaks: Troubleshooting and Solution

## Context Chapter: 3
## Context Title: Sachets Formation and Sealing

To address the issue of sachets leaking product, it is essential to ensure that the sealing process is optimal. The sachet guide rollers (optional) in the last section of the sealing system play a crucial role in guiding the sachets correctly onto the conveyor belt below [4.2.6]. This highlights the importance of proper installation and adjustment of these rollers.

Moreover, the longitudinal sealing station, which involves using sealing rollers (Fig. 23), is also crucial for ensuring proper sealing. The pressure of the rollers can be adjusted by operating on the screw M10 (Fig. 24). However, if leaks persist, it may be necessary to investigate further and perform additional troubleshooting steps.

Before proceeding with any adjustments or repairs, please ensure that all manual commands are disabled, and voltage has been removed as indicated in bold. Always follow safety guidelines and precautions when working with the machine.

If you're unsure about any part of the process or if leaks persist after attempting these steps, it is recommended to consult the manufacturer's support team for further assistance.

---
---
# Question The reel unwinder does not move properly, we often have alarms related to it, what can I do?
Response: ## Troubleshooting Reel Unwinder Issues

### A168 - FILM BROKEN: The dancing roller of the unwinder has reached the lowest position; Check the unwinder.

To resolve this issue, you should check the unwinder to ensure it is functioning properly.

---
---
# Question When i change some parameter on the panel the machine doesn't react. what can be the problem?
Response: A common problem!

When you change a parameter on the panel but the machine doesn't react, there are several possible causes:

1. **Machine not logged in**: Make sure the machine is properly logged in at the required level (e.g., Level 1 or higher). If it's not logged in, the machine won't respond to panel changes.
2. **Parameter update not confirmed**: In some cases, the machine may require a confirmation before updating its settings. Check for any pop-up messages or prompts that require user input (e.g., "Apply" or "OK").
3. **Panel not updated**: Ensure that the panel is properly synchronized with the machine's PLC (Programmable Logic Controller) software. If there's a delay in updating the panel, try restarting the machine or refreshing the panel.
4. **Invalid parameter range**: Verify that the new value entered on the panel is within an allowed range for the specific parameter. If not, try adjusting the value to fall within the valid range.
5. **Machine stuck in a state**: It's possible that the machine has locked up or become stuck in a certain mode (e.g., " Maintenance Mode"). Check the machine's status display (if available) to see if it's indicating any errors or warnings.
6. **PLC software not updated**: Ensure that the PLC software is up-to-date and consistent with the panel configuration. If the PLC software is outdated, updating it might resolve the issue.

To troubleshoot further:

1. Consult the machine's manual or documentation for specific instructions on configuring parameters.
2. Check the panel's display for any error messages or warnings.
3. Try restarting the machine or refreshing the panel to ensure synchronization is updated correctly.
4. Contact your machine manufacturer or a qualified technician if you're unsure about a particular issue.

Remember, always work in a controlled and safe environment when interacting with machinery.
