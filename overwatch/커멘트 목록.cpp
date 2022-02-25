variables
{
	player:
		27: text
}

rule("create HUD")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	action
	{
		Event Player.text = False;
		Create HUD Text(Filtered Array(Event Player, !Event Player.text), Null, Null, Custom String("[+] 커맨드 목록 보기 : {0}              ",
			Input Binding String(Button(Interact))), Right, 0, Color(White), Color(White), Color(White), Visible To and String,
			Default Visibility);
		Create HUD Text(Filtered Array(Event Player, Event Player.text), Null, Null, Custom String(
			"[-] 커맨드 목록 보기 : {0}\r\n      {1} + (A/AW/W/WD/D)\r\n      {2} + {1} + (A/AW/W/WD/D)", Input Binding String(Button(Interact)),
			Input Binding String(Button(Melee)), Input Binding String(Button(Secondary Fire))), Right, 0, Color(White), Color(White),
			Color(White), Visible To and String, Default Visibility);
	}
}

rule("is Button Held")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	condition
	{
		Is Button Held(Event Player, Button(Interact)) == True;
	}

	action
	{
		Event Player.text = True;
		Wait Until(!Is Button Held(Event Player, Button(Interact)), 99999);
		Event Player.text = False;
	}
}