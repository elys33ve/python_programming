"""
calculates dmg of some talents for characters stats bc sure
- doesn't take weapon, other artifact, resonance, etc. buffs into account
- also doesnt take enemy resistance bc i got bored
"""
lvl_multiplier = [1, 34.14, 80.58, 136.29, 207.38, 323.60, 492.88, 765.64, 1077.44, 1446.85]		# level multiplier for transformative reactions



### get input stats
def stats():
	atk = float(input("attack = "))
	em = float(input("elemental mastery = "))
	cr = float(input("crit rate = "))
	cd = float(input("crit dmg = "))

	if cr > 5:				# if input as %, change to decimal
		cr /= 100
	if cd > 5:
		cd = (cd / 100)
	cd += 1

	return atk, em, cr, cd


### swirl dmg
def swirl(em, lvl=90):
	lvl = lvl_multiplier[int((lvl-(lvl%10))/10)]

	rm = 0.6		# reaction multiplier
	rb = 0.6		# reaction bonus (w viridescent bonus = 0.6)
	lm = lvl		# lvl multiplier (lvl 90 = 1446.85)
	erm = 1			# enemy resistance multiplier

	dmg = rm * lm * (1 + ( (16 * em) / (2000 + em) ) + rb) * erm
	return dmg


### calculate skill/talent
def skill(atk, cr, cd, talent, add=0):
	dmg = (talent * atk) + add
	crit = dmg * cd
	avg = ((crit * cr) + (dmg * (1-cr)))

	return dmg, crit, avg


### display skill
def disp_talent(talent, dmg, crit, avg, tabs=['','','']):
	dmg_t, crit_t = "\t\t", "\t\t"

	if dmg > 10000:								# adjust dmg tab
		dmg_t = "\t"
	if crit > 10000:							# adjust crit tab
		crit_t = f"\t"

	if crit == 0:
		crit = "  --  "
	else:
		crit = f"{crit:.2f}"
	if avg == 0:
		avg = "  --  "
	else:
		avg = f"{avg:.2f}"
	
	print(f"{talent}:  \t{tabs[0]}{dmg:.2f}{tabs[1]}{dmg_t}{crit}{tabs[2]}{crit_t}{avg}")


### -----------------------------
# (without extra buffs from weapons, artifacts, etc.)


### venti
def venti(atk, em, cr, cd):
	swirl_dmg = swirl(em)
	e_press = skill(atk, cr, cd, 4.97)
	e_hold = skill(atk, cr, cd, 6.84)
	burst = skill(atk, cr, cd, 0.677)

	print("\n----- venti -----")
	print(f"swirl dmg = {swirl_dmg:.2f}")
	print("\t\t-- dmg --\t-- crit --\t-- avg --")
	disp_talent("e press", e_press[0], e_press[1], e_press[2])
	disp_talent("e hold",  e_hold[0], e_hold[1], e_hold[2])
	disp_talent("burst", burst[0], burst[1], burst[2])
	print()


### sayu
def sayu (atk, em, cr, cd, lvl=90):
	swirl_dmg = swirl(em, lvl)
	windwheel = skill(atk, cr, cd, 0.765)
	ww_press = skill(atk, cr, cd, 3.366)
	ww_hold = skill(atk, cr, cd, 4.624)
	windwheel_ele = skill(atk, cr, cd, 0.357)
	ww_ele = skill(atk, cr, cd, 1.6184)

	initial_dmg = skill(atk, cr, cd, 2.482)
	initial_heal = skill(atk, cr, cd, 1.9584, 1587)
	burst_dmg = skill(atk, cr, cd, 1.105)
	burst_heal = skill(atk, cr, cd, 1.6973, 1376)

	print("\n----- sayu -----")
	print(f"swirl dmg = {swirl_dmg:.2f}")
	print()
	print("-skill-\t\t\t-- dmg --\t-- crit --\t-- avg --")
	disp_talent("whindwheel", windwheel[0], windwheel[1], windwheel[2], ['\t','',''])
	disp_talent("windwheel press", ww_press[0], ww_press[1], ww_press[2])
	disp_talent("windwheel hold", ww_hold[0], ww_hold[1], ww_hold[2])
	disp_talent("windwheel elemental", windwheel_ele[0], 0, 0)
	disp_talent("whirlwind elemental", ww_ele[0], 0, 0)
	print()
	print("-burst-\t\t\t-- dmg --\t-- crit --\t-- avg --")
	disp_talent("activation dmg", initial_dmg[0], initial_dmg[1], initial_dmg[2])
	disp_talent("activation heal", initial_heal[0], 0, 0)
	disp_talent("burst dmg", burst_dmg[0], burst_dmg[1], burst_dmg[2], ['\t','',''])
	disp_talent("burst heal", burst_heal[0], 0, 0, ['\t','',''])


### heizou
def heizou(atk, em, cr, cd):
	na = [0.675, 0.663, 0.919, [0.266, 0.293, 0.346], 1.106]

	swirl_dmg = swirl(em)
	e_press = skill(atk, cr, cd, 4.385)
	ca = skill(atk, cr, cd, 1.314)
	burst = skill(atk, cr, cd, 6.687)

	for i in range(5):
		if i == 3:
			for j in range(3):
				na[i][j] = skill(atk, cr, cd, na[i][j])
		else:
			na[i] = skill(atk, cr, cd, na[i])

	print("\n----- heizou -----")
	print(f"swirl dmg = {swirl_dmg:.2f}")
	print("\t\t-- dmg --\t-- crit --\t-- avg --")
	disp_talent("e press", e_press[0], e_press[1], e_press[2])
	disp_talent("burst", burst[0], burst[1], burst[2])
	disp_talent("charged", ca[0], ca[1], ca[2])

	na_dmg = "dmg:"
	na_crit = "crit:"
	na_avg = "avg:"
	print("\nnormal attack:")
	for i in range(5):
		if i == 3:
			na_dmg += f"\t\t{na[i][0][0]:.2f} + {na[i][1][0]:.2f} + {na[i][2][0]:.2f}"
			na_crit += f"\t\t{na[i][0][1]:.2f} + {na[i][1][1]:.2f} + {na[i][2][1]:.2f}"
			na_avg += f"\t\t{na[i][0][2]:.2f} + {na[i][1][2]:.2f} + {na[i][2][2]:.2f}"
		else:
			na_dmg += (f"\t\t{na[i][0]:.2f}")
			na_crit += (f"\t\t{na[i][1]:.2f}")
			na_avg += (f"\t\t{na[i][2]:.2f}")
	print(na_dmg)
	print(na_crit)
	print(na_avg)






if __name__ == "__main__":
	#inputs = stats()
	#atk, em, cr, cd = inputs[0], inputs[1], inputs[2], inputs[3]
	weapon = 674
	s90 = [244+weapon, 96, 0.05, 1.50]

	atk = s90[0] + (s90[0] * (0.152 + 0.053)) + 40
	em = s90[1] + 228 + 187 + 187 + 165
	cr = s90[2]
	cd = s90[3]

	sayu(atk, em, cr, cd)