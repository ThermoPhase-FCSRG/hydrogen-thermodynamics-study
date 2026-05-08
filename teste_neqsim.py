from neqsim.thermo import fluid

# Create a natural gas fluid
fl = fluid('srk')
fl.addComponent('methane', 0.85)
fl.addComponent('ethane', 0.10)
fl.addComponent('propane', 0.05)
fl.setTemperature(25.0, 'C')
fl.setPressure(60.0, 'bara')
fl.setMixingRule('classic')

from neqsim.thermo import TPflash, printFrame
TPflash(fl)
printFrame(fl)