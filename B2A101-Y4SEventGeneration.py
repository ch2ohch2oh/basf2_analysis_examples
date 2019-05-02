#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################
#
# Stuck? Ask for help at questions.belle2.org
#
# Y(4S) -> BBbar event generation
#
# This tutorial demonstrates how to generate
#
# e+e- -> Y(4S) -> BBbar
#
# events with EvtGen in BASF2, where the decay of Y(4S)
# is specified by the given .dec file.
#
# The generated events are saved to the output ROOT file.
# In each event the generated particles (MCParticle objects)
# are stored in the StoreArray<MCParticle>.
#
# Contributors: A. Zupanc (June 2014), I.Komarov (Sept. 2018)
#
######################################################

import basf2 as b2
import generators as ge
import modularAnalysis as ma

# generation of 100 events according to the specified DECAY table
# Y(4S) -> Btag- Bsig+
# Btag- -> D0 pi-; D0 -> K- pi+
# Bsig+ -> mu+ nu_mu
#

# Defining custom path
my_path = b2.create_path()

# Setting up number of events to generate
# This is needed before you generate any events
ma.setupEventInfo(noEvents=10, path=my_path)

# Adding genberator
# This specific event generator will generate either charged final states (charged B mesons)
# or mixed final states (neutal B mesons)
ge.add_evtgen_generator(path=my_path,
                        finalstate='signal',
                        signaldecfile=b2.find_file(
                            'analysis/examples/tutorials/B2A101-Y4SEventGeneration.dec'))

# Set the first parameter to zero if you want to see all the events.
# This will show how many particles are generated in each event.
ma.printDataStore(0, path=my_path)
# Show the decay chain in each event
ma.printMCParticles(path=my_path)

# dump generated events in DST format to the output ROOT file
#
my_path.add_module('RootOutput', outputFileName='with_gearbox_1000.root')

# process all modules added to the analysis_main path
# (note: analysis_main is the default path created in the modularAnalysis.py)
b2.process(path=my_path)

# print out the summary
print(b2.statistics)


