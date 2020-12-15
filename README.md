# Advent of Code 2020

## Day 1: Report Repair

After saving Christmas **five years in a row**,
you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish;
the locals just call them **stars**. None of the currency exchanges seem to have heard of them,
but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all **fifty stars** by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

Before you leave, the Elves in accounting just need you to fix your **expense report** (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to **find the two entries that sum to 2020** and then multiply those two numbers together.

**Find the two entries that sum to 2020; what do you get if you multiply them together?**

### Part Two

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation.
They offer you a second one if you can find **three numbers** in your expense report that meet the same criteria.

In your expense report, **what is the product of the three entries that sum to 2020?**

## Day 2: Password Philosophy

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via **toboggan**.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the
Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of **passwords**
(according to the corrupted database) and **the corporate policy when that password was set**.

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

**How many passwords are valid** according to their policies?

### Part Two

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two **positions in the password**, where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
**Exactly one of these positions** must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

## Day 3: Toboggan Trajectory

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

> ..##.......
> #...#...#..
> .#....#..#.
> ..#.#...#.#
> .#...##..#.
> ..#.##.....
> .#.#.#....#
> .#........#
> #.##...#...
> #...##....#
> .#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

> ..##.........##.........##.........##.........##.........##....... --->
> #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
> .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
> ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
> .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
> ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##..... --->
> .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
> .#........#.#........#.#........#.#........#.#........#.#........#
> #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
> #...##....##...##....##...##....##...##....##...##....##...##....#
> .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.# --->

You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by **counting all the trees** you would encounter for the slope **right 3, down 1**:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

> ..##.........##.........##.........##.........##.........##....... --->
> #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
> .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
> ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
> .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
> ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##..... --->
> .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
> .#........#.#........X.#........#.#........#.#........#.#........#
> #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
> #...##....##...##....##...#X....##...##....##...##....##...##....#
> .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.# --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, **how many trees would you encounter?**

## Day 10: Adapter Array

Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm.
Before you can figure out whether it will impact your vacation plans, however, your device suddenly turns off!

Its battery is dead.

You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong number of **jolts**.
Always prepared, you make a list of all of the joltage adapters in your bag.

Each of your joltage adapters is rated for a specific **output joltage** (your puzzle input).
Any given adapter can take an input 1, 2, or 3 jolts **lower** than its rating and still produce its rated output joltage.

In addition, your device has a built-in joltage adapter rated for **3 jolts higher** than the highest-rated adapter in your bag.
(If your adapter list were 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)

Treat the charging outlet near your seat as having an effective joltage rating of 0.

Since you have some time to kill, you might as well test all of your adapters.
Wouldn't want to get to your resort and realize you can't even charge your device!

If you **use every adapter in your bag** at once, what is the distribution of joltage differences
between the charging outlet, the adapters, and your device?

Because adapters can only connect to a source 1-3 jolts lower than its rating,
in order to use every adapter, you'd need to choose them like this:

- The charging outlet has an effective rating of 0 jolts, so the only adapters that could connect to it directly
- would need to have a joltage rating of 1, 2, or 3 jolts. Of these, only one you have is an adapter rated 1 jolt (difference of 1).
- From your 1-jolt rated adapter, the only choice is your 4-jolt rated adapter (difference of 3).
- From the 4-jolt rated adapter, the adapters rated 5, 6, or 7 are valid choices. However, in order to not skip any adapters,
- you have to pick the adapter rated 5 jolts (difference of 1).
- Similarly, the next choices would need to be the adapter rated 6 and then the adapter rated 7 (with difference of 1 and 1).
- The only adapter that works with the 7-jolt rated adapter is the one rated 10 jolts (difference of 3).
- From 10, the choices are 11 or 12; choose 11 (difference of 1) and then 12 (difference of 1).
- After 12, only valid adapter has a rating of 15 (difference of 3), then 16 (difference of 1), then 19 (difference of 3).
- Finally, your device's built-in adapter is always 3 higher than the highest adapter, so its rating is 22 jolts (always a difference of 3).

In this example, when using every adapter, there are 7 differences of 1 jolt and 5 differences of 3 jolts.

Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count the joltage
differences between the charging outlet, the adapters, and your device.

**What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?**

### Part Two

To completely determine whether you have enough adapters, you'll need to figure out how many different ways they can be arranged.
Every arrangement needs to connect the charging outlet to your device. The previous rules about when adapters can successfully connect still apply.

You glance back down at your bag and try to remember why you brought so many adapters;
there must be **more than a trillion** valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

**What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?**

## Day 11: Seating System

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

- If a seat is **empty** (L) and there are **no** occupied seats adjacent to it, the seat becomes **occupied**.
- If a seat is **occupied** (#) and **four or more** seats adjacent to it are also occupied, the seat becomes **empty**.
- Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

At a certain point, the chaos stabilizes and further applications of these rules cause no seats to change state!

Simulate your seating area by applying the seating rules repeatedly until no seats change state. **How many seats end up occupied?**

### Part Two

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats _-_
they care about **the first seat they can see** in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the **first seat** in each of those eight directions.

Also, people seem to be more tolerant than you expected: it now takes **five or more** visible occupied seats for an occupied seat to become empty
(rather than **four or more** from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied,
seats matching no rule don't change, and floor never changes.

Again, people stop shifting around and the seating area reaches equilibrium.

Given the new visibility method and the rule change for occupied seats becoming empty,
once equilibrium is reached, **how many seats end up occupied?**

## Day 12: Rain Risk

Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take **evasive actions!**

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety,
it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character **actions** paired with integer input **values.**
After staring at them for a few minutes, you work out what they probably mean:

- Action N means to move north by the given value.
- Action S means to move south by the given value.
- Action E means to move east by the given value.
- Action W means to move west by the given value.
- Action L means to turn left the given number of degrees.
- Action R means to turn right the given number of degrees.
- Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing **east**. Only the L and R actions change the direction the ship is facing.
(That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

Figure out where the navigation instructions lead. **What is the Manhattan distance between that location and the ship's starting position?**

### Part Two

Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a **waypoint** which is relative to the ship's position:

- Action N means to move the waypoint north by the given value.
- Action S means to move the waypoint south by the given value.
- Action E means to move the waypoint east by the given value.
- Action W means to move the waypoint west by the given value.
- Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
- Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
- Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts **10 units east and 1 unit north** relative to the ship.
The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

Figure out where the navigation instructions actually lead.
**What is the Manhattan distance between that location and the ship's starting position?**

## Day 13: Shuttle Search

Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book another ship,
you discover that no ships embark from that port to your vacation island.
You'll need to get from the port to the nearest airport.

Fortunately, a shuttle bus service is available to bring you from the sea port to the airport!
Each bus has an ID number that also indicates **how often the bus leaves for the airport.**

Bus schedules are defined based on a **timestamp** that measures the **number of minutes** since some fixed reference point in the past.
At timestamp 0, every bus simultaneously departed from the sea port. After that, each bus travels to the airport,
then various other locations, and finally returns to the sea port to repeat its journey forever.

The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on.
The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when the bus departs, you can ride that bus to the airport!

Your notes (your puzzle input) consist of two lines. The first line is your estimate of the **earliest timestamp you could depart on a bus.**
The second line lists the bus IDs that are in service according to the shuttle company; entries that show x must be out of service, so you decide to ignore them.

To save time once you arrive, your goal is to figure out **the earliest bus you can take to the airport.** (There will be exactly one such bus.)

**What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?**

### Part Two

The shuttle company is running a contest: one gold coin for anyone that can find the earliest timestamp
such that the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute.
(The first line in your input is no longer relevant.)

**What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?**

## Day 14: Docking Data

As your ferry approaches the sea port, the captain asks for your help again. The computer system that runs this port isn't compatible with the docking program on the ferry,
so the docking parameters aren't being correctly initialized in the docking program's memory.

After a brief inspection, you discover that the sea port's computer system uses a strange **bitmask** system in its initialization program.
Although you don't have the correct decoder chip handy, you can emulate it in software!

The initialization program (your puzzle input) can either update the bitmask or write a value to memory. Values and memory addresses are both 36-bit unsigned integers.
For example, ignoring bitmasks for a moment, a line like mem[8] = 11 would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in the value, while an X leaves the bit in the value unchanged.

**Execute the initialization program. What is the sum of all values left in memory after it completes?**

### Part Two

For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a **memory address decoder.** Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination **memory address** in the following way:

- If the bitmask bit is 0, the corresponding memory address bit is **unchanged.**
- If the bitmask bit is 1, the corresponding memory address bit is **overwritten with 1.**
- If the bitmask bit is X, the corresponding memory address bit is **floating.**

A **floating** bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on **all possible values**, potentially causing many memory addresses to be written all at once!

Execute the initialization program using an emulator for a version 2 decoder chip. **What is the sum of all values left in memory after it completes?**
