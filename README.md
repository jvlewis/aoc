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

\*How many passwords are valid\*\* according to their policies?

### Part Two

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two **positions in the password**, where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
**Exactly one of these positions** must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

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

The charging outlet has an effective rating of 0 jolts, so the only adapters that could connect to it directly
would need to have a joltage rating of 1, 2, or 3 jolts. Of these, only one you have is an adapter rated 1 jolt (difference of 1).
From your 1-jolt rated adapter, the only choice is your 4-jolt rated adapter (difference of 3).
From the 4-jolt rated adapter, the adapters rated 5, 6, or 7 are valid choices. However, in order to not skip any adapters,
you have to pick the adapter rated 5 jolts (difference of 1).
Similarly, the next choices would need to be the adapter rated 6 and then the adapter rated 7 (with difference of 1 and 1).
The only adapter that works with the 7-jolt rated adapter is the one rated 10 jolts (difference of 3).
From 10, the choices are 11 or 12; choose 11 (difference of 1) and then 12 (difference of 1).
After 12, only valid adapter has a rating of 15 (difference of 3), then 16 (difference of 1), then 19 (difference of 3).
Finally, your device's built-in adapter is always 3 higher than the highest adapter, so its rating is 22 jolts (always a difference of 3).
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

-If a seat is **empty** (L) and there are **no** occupied seats adjacent to it, the seat becomes **occupied**.
-If a seat is **occupied** (#) and **four or more** seats adjacent to it are also occupied, the seat becomes **empty**.
-Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

At a certain point, the chaos stabilizes and further applications of these rules cause no seats to change state!

Simulate your seating area by applying the seating rules repeatedly until no seats change state. **How many seats end up occupied?**

### Part Two

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats -
they care about **the first seat they can see** in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the **first seat** in each of those eight directions.

Also, people seem to be more tolerant than you expected: it now takes **five or more** visible occupied seats for an occupied seat to become empty
(rather than **four or more** from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied,
seats matching no rule don't change, and floor never changes.

Again, people stop shifting around and the seating area reaches equilibrium.

Given the new visibility method and the rule change for occupied seats becoming empty,
once equilibrium is reached, **how many seats end up occupied?**
