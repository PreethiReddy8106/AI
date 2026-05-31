def get_response(userText):

    text = userText.lower()

    # ------------------------
    # BIKE TERMS
    # ------------------------

    if "torque" in text:
        return """🏍️ Torque is the pulling force produced by the engine.
Higher torque helps with acceleration and climbing hills."""

    elif "bhp" in text:
        return """🏍️ BHP (Brake Horsepower) measures engine power.
More BHP usually means higher top speed."""

    elif "abs" in text:
        return """🏍️ ABS (Anti-lock Braking System) prevents wheel lock during sudden braking and improves safety."""

    elif "cc" in text:
        return """🏍️ CC (Cubic Capacity) indicates engine displacement.
Higher CC usually means more power."""

    elif "rpm" in text:
        return """🏍️ RPM means Revolutions Per Minute.
It shows how fast the engine is spinning."""

    # ------------------------
    # TROUBLESHOOTING
    # ------------------------

    elif "not starting" in text or "won't start" in text or "wont start" in text:

        return """🔧 Possible causes:

• Weak Battery
• Faulty Spark Plug
• Fuel Supply Issue
• Starter Motor Problem

Recommended Checks:
✓ Battery
✓ Spark Plug
✓ Fuel Level"""

    elif "clicking sound" in text:

        return """🔧 Clicking sound usually indicates:

• Weak Battery
• Loose Battery Connection
• Starter Relay Issue"""

    elif "overheating" in text or "engine hot" in text:

        return """🌡️ Engine Overheating Possible Causes:

• Low Coolant
• Low Engine Oil
• Blocked Radiator
• Continuous High RPM Riding"""

    elif "brake noise" in text or "brake problem" in text:

        return """🛑 Check:

• Brake Pads
• Brake Fluid
• Brake Disc Condition"""

    # ------------------------
    # SPARE PARTS
    # ------------------------

    elif "battery" in text:

        return """🔋 Bike Battery

Functions:
• Starts Engine
• Powers Lights
• Supports Electronics"""

    elif "spark plug" in text:

        return """⚡ Spark Plug

Ignites the air-fuel mixture inside the engine cylinder."""

    elif "brake pads" in text:

        return """🛑 Brake Pads

Generate friction against the brake disc to stop the bike."""

    elif "chain" in text:

        return """⛓️ Bike Chain

Transfers engine power to the rear wheel."""

    # ------------------------
    # MAINTENANCE
    # ------------------------

    elif "engine oil" in text:

        return """🛠️ Engine Oil

Change every 3000–5000 km depending on riding conditions."""

    elif "tire pressure" in text:

        return """🛞 Proper tire pressure improves:

• Mileage
• Stability
• Tire Life
• Safety"""

    elif "service" in text:

        return """🛠️ Regular Service Checklist:

✓ Engine Oil
✓ Air Filter
✓ Brake Inspection
✓ Chain Lubrication
✓ Tire Pressure"""

    # ------------------------
    # RECOMMENDATIONS
    # ------------------------

    elif "sports bike" in text:

        return """🏍️ Sports Bike Recommendations

1. Yamaha R15 V4
2. KTM Duke 200
3. Bajaj Pulsar RS200

Great performance and handling."""

    elif "mileage bike" in text:

        return """⛽ Mileage Bike Recommendations

1. Honda SP125
2. TVS Raider
3. Bajaj Platina

Excellent fuel efficiency."""

    elif "cruiser bike" in text:

        return """🛣️ Cruiser Bike Recommendations

1. Royal Enfield Classic 350
2. Honda Hness CB350
3. Royal Enfield Meteor 350"""

    elif "best bike" in text:

        return """🏍️ Please specify:

• Sports Bike
• Mileage Bike
• Cruiser Bike

and I'll recommend one."""

    # ------------------------
    # GREETINGS
    # ------------------------

    elif text in ["hi", "hello", "hey"]:

        return """👋 Hello Rider!

I can help with:

🏍️ Bike Terms
🔧 Troubleshooting
⚙️ Spare Parts
🛠️ Maintenance
🚀 Recommendations"""

    # ------------------------
    # DEFAULT
    # ------------------------

    else:

        return """🤖 I don't know that yet.

Try asking about:

🏍️ Torque
🏍️ ABS
🔧 Bike not starting
⚙️ Spark Plug
🛠️ Engine Oil
🚀 Sports Bike Recommendations"""
