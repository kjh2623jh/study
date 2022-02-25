rule("텔포")
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
		Teleport(Event Player, Ray Cast Hit Position(Eye Position(Event Player), Eye Position(Event Player) + Facing Direction Of(
			Event Player) * 999, All Players(All Teams), All Players(All Teams), False) + Vector(0, Absolute Value(Eye Position(
			Event Player) + Position Of(Event Player) * -1), 0) * -1 + Facing Direction Of(Event Player) * -1);
	}
}


//텔레포트. 캐릭터의 발과 눈 사이의 거리만큼 더 위쪽으로 텔포됨.
Teleport(Event Player, Ray Cast Hit Position(Eye Position(Event Player), Eye Position(Event Player) + Facing Direction Of(
    Event Player) * 999, All Players(All Teams), All Players(All Teams), False));


//오차 없앰.
Teleport(Event Player, Position Of(Event Player) + Vector(0, Absolute Value(Eye Position(Event Player) + Position Of(
    Event Player) * -1), 0) * -1);
    
Teleport(Event Player, Ray Cast Hit Position(Eye Position(Event Player), Eye Position(Event Player) + Facing Direction Of(
    Event Player) * 999, All Players(All Teams), All Players(All Teams), False) + Vector(0, Absolute Value(Eye Position(
    Event Player) + Position Of(Event Player) * -1), 0) * -1);


//벽 뚫는거 방지 추가
Teleport(Event Player, Position Of(Event Player) + Facing Direction Of(Event Player) * -1);

Teleport(Event Player, Ray Cast Hit Position(Eye Position(Event Player), Eye Position(Event Player) + Facing Direction Of(
    Event Player) * 999, All Players(All Teams), All Players(All Teams), False) + Vector(0, Absolute Value(Eye Position(
    Event Player) + Position Of(Event Player) * -1), 0) * -1 + Facing Direction Of(Event Player) * -1);