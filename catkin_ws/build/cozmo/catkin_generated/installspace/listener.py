#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int8
import cozmo
import random
import cv2
import numpy as np
import asyncio
import math
from cozmo.util import distance_mm, speed_mmps, degrees
import time

cozmo.robot.Robot.drive_off_charger_on_connect = True


def action1_happy(robot: cozmo.robot.Robot):
    pose = robot.pose
    random_selection = random.randint(1, 5)
    if random_selection == 1:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy).wait_for_completed()
    if random_selection == 2:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabExcited).wait_for_completed()
    if random_selection == 3:
        robot.play_anim(name="anim_peekaboo_success_02").wait_for_completed()
    if random_selection == 4:
        robot.play_anim(name="anim_peekaboo_success_03").wait_for_completed()
    if random_selection == 5:
        robot.play_anim(name="anim_sparking_success_02").wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()
    # charge = robot.is_charging
    # print("Charging:", charge)
    # battery = robot.battery_voltage
    # print("Battery1:", battery)
    # # time.sleep(30)
    # battery = robot.battery_voltage
    # print("Battery:2", battery)


def action2_sad(robot: cozmo.robot.Robot):
    pose = robot.pose
    random_selection = random.randint(1, 5)
    if random_selection == 1:
        robot.play_anim(name="anim_fistbump_fail_01").wait_for_completed()
    if random_selection == 2:
        robot.play_anim(name="anim_memorymatch_failgame_cozmo_03").wait_for_completed()
    if random_selection == 3:
        robot.play_anim(name="anim_reacttocliff_turtlerollfail_02").wait_for_completed()
    if random_selection == 4:
        robot.play_anim(name="anim_bored_event_01").wait_for_completed()
    if random_selection == 5:
        robot.play_anim(name="anim_speedtap_losegame_intensity02_01").wait_for_completed()  #ends with fork lifted up
        robot.set_lift_height(0.0).wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()


def action3_angry(robot: cozmo.robot.Robot):
    pose = robot.pose
    random_selection = random.randint(1, 5)
    if random_selection == 1:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated).wait_for_completed()
    if random_selection == 2:
        robot.play_anim(name="anim_pyramid_reacttocube_frustrated_high_01").wait_for_completed()
    if random_selection == 3:
        robot.play_anim(name="anim_majorfail").wait_for_completed()
    if random_selection == 4:
        robot.play_anim(name="anim_memorymatch_failgame_cozmo_01").wait_for_completed()
    if random_selection == 5:
        robot.play_anim(name="anim_memorymatch_failgame_cozmo_02").wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()

def action4_shocked(robot: cozmo.robot.Robot):
    pose = robot.pose
    random_selection = random.randint(1, 3)
    if random_selection == 1:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabScaredCozmo).wait_for_completed()
    if random_selection == 2:
        robot.play_anim(name="anim_dizzy_reaction_hard_01").wait_for_completed()
    if random_selection == 3:
        robot.play_anim(name="anim_dizzy_reaction_medium_01").wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()

def action5_monster(robot: cozmo.robot.Robot):
    pose = robot.pose
    random_selection = random.randint(1, 2)
    if random_selection == 1:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabZombie).wait_for_completed()
    if random_selection == 2:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabVampire).wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()

def action6_animal(robot: cozmo.robot.Robot):
    pose = robot.pose
    random_selection = random.randint(1, 6)
    if random_selection == 1:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDog).wait_for_completed()
    if random_selection == 2:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabCat).wait_for_completed()
    if random_selection == 3:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabRattleSnake).wait_for_completed()
    if random_selection == 4:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabElephant).wait_for_completed()
    if random_selection == 5:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabTiger).wait_for_completed()
    if random_selection == 6:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabChicken).wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()

def action7_hyperactive(robot: cozmo.robot.Robot):
    pose = robot.pose
    random_selection = random.randint(1, 2)
    if random_selection == 1:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFireTruck).wait_for_completed()
    if random_selection == 2:
        robot.play_anim(name="anim_dancing_mambo_01").wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()

def action8_ill(robot: cozmo.robot.Robot):
    pose = robot.pose
    random_selection = random.randint(1, 3)
    if random_selection == 1:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHiccup).wait_for_completed()
    if random_selection == 2:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSneeze).wait_for_completed()
    if random_selection == 3:
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDizzy).wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()

def action9_song(robot: cozmo.robot.Robot):
    pose = robot.pose
    random_selection = random.randint(1, 3)
    if random_selection == 1:
        robot.play_anim(name="anim_cozmosings_80_song_01").wait_for_completed()
    if random_selection == 2:
        robot.play_anim(name="anim_cozmosings_100_song_01").wait_for_completed()
    if random_selection == 3:
        robot.play_anim(name="anim_cozmosings_120_song_01").wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()

def action10_joke(robot: cozmo.robot.Robot):
    pose = robot.pose
    robot.say_text("I have a joke for you!").wait_for_completed()
    random_selection = random.randint(1, 25)
    if random_selection == 1:
        robot.say_text("Did you hear about the new restaurant called Karma?").wait_for_completed()
        robot.say_text("There’s no menu. You get what you deserve!").wait_for_completed()
    if random_selection == 2:
        robot.say_text("Did you hear about the claustrophobic astronaut?").wait_for_completed()
        robot.say_text("He just needed a little space!").wait_for_completed()
    if random_selection == 3:
        robot.say_text("What do you call a fake noodle?").wait_for_completed()
        robot.say_text("An impasta!").wait_for_completed()
    if random_selection == 4:
        robot.say_text("Why did the chicken cross the road?").wait_for_completed()
        robot.say_text("To get to KFC!").wait_for_completed()
    if random_selection == 5:
        robot.say_text("What did the cheese say when he looked in the mirror?").wait_for_completed()
        robot.say_text("Halloumi!").wait_for_completed()
    if random_selection == 6:
        robot.say_text("What do you call a bear without any teeth?").wait_for_completed()
        robot.say_text("A gummy bear!").wait_for_completed()
    if random_selection == 7:
        robot.say_text("What do you get when you cross a snowman with a vampire?").wait_for_completed()
        robot.say_text(" Frostbite!").wait_for_completed()
    if random_selection == 8:
        robot.say_text("Why don’t they play poker in the jungle?").wait_for_completed()
        robot.say_text("Too many cheetahs!").wait_for_completed()
    if random_selection == 9:
        robot.say_text("Why did the golfer change his pants?").wait_for_completed()
        robot.say_text("Because he got a hole in one!").wait_for_completed()
    if random_selection == 10:
        robot.say_text("Why did the ruler get fired?").wait_for_completed()
        robot.say_text("Because he couldn’t measure up!").wait_for_completed()
    if random_selection == 11:
        robot.say_text("Why did Cinderella get kicked off the football team?").wait_for_completed()
        robot.say_text("Because she kept running from the ball!").wait_for_completed()
    if random_selection == 12:
        robot.say_text("Parallel lines have so much in common. It’s a shame they’ll never meet!").wait_for_completed()
    if random_selection == 13:
        robot.say_text("Why don’t scientists trust atoms?").wait_for_completed()
        robot.say_text(" Because they make up everything!").wait_for_completed()
    if random_selection == 14:
        robot.say_text("Why did the gym close down?").wait_for_completed()
        robot.say_text("It just didn’t work out!").wait_for_completed()
    if random_selection == 15:
        robot.say_text("Two artists had an art contest. It ended in a draw!").wait_for_completed()
    if random_selection == 16:
        robot.say_text("I have a fear of speed bumps. But I am slowly getting over it!").wait_for_completed()
    if random_selection == 17:
        robot.say_text("Why are ghosts such bad liars?").wait_for_completed()
        robot.say_text("Because they are easy to see through!").wait_for_completed()
    if random_selection == 18:
        robot.say_text("Where do fish sleep?").wait_for_completed()
        robot.say_text("In the river bed!").wait_for_completed()
    if random_selection == 19:
        robot.say_text("What did one plate say to his friend?").wait_for_completed()
        robot.say_text("Tonight, dinner’s on me!").wait_for_completed()
    if random_selection == 20:
        robot.say_text("Where are average things manufactured?").wait_for_completed()
        robot.say_text("The satis factory!").wait_for_completed()
    if random_selection == 21:
        robot.say_text("What’s red and moves up and down?").wait_for_completed()
        robot.say_text("A tomato in an elevator!").wait_for_completed()
    if random_selection == 22:
        robot.say_text("Why doesn’t the sun go to college?").wait_for_completed()
        robot.say_text("Because it has a million degrees!").wait_for_completed()
    if random_selection == 23:
        robot.say_text("Why are skeletons so calm?").wait_for_completed()
        robot.say_text("Because nothing gets under their skin!").wait_for_completed()
    if random_selection == 24:
        robot.say_text("How do trees get online?").wait_for_completed()
        robot.say_text("They just log on!").wait_for_completed()
    if random_selection == 25:
        robot.say_text("Why did the orange stop?").wait_for_completed()
        robot.say_text("It ran out of juice!").wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()

def action11_reminder(robot: cozmo.robot.Robot):
    pose = robot.pose
    robot.say_text("I have a friendly reminder for you!").wait_for_completed()
    random_selection = random.randint(1, 5)
    if random_selection == 1:
        robot.say_text("Don’t forget to drink a glass of water to stay hydrated!").wait_for_completed()
    if random_selection == 2:
        robot.say_text("Remember to stretch your legs if you’ve been sitting down for too long!").wait_for_completed()
    if random_selection == 3:
        robot.say_text("If you’re feeling hungry, eat a healthy snack!").wait_for_completed()
    if random_selection == 4:
        robot.say_text("Remember, it’s healthy to take regular breaks from your work!").wait_for_completed()
    if random_selection == 5:
        robot.say_text("If you need to take a break, how about going for a nice walk outside!").wait_for_completed()
    robot.go_to_pose(pose).wait_for_completed()

def action12_handinteraction(robot: cozmo.robot.Robot):
    pose = robot.pose
    #Pounce on finger
    robot.say_text("Move your finger around in front of me!").wait_for_completed()
    pounce = robot.start_behavior(cozmo.behavior.BehaviorTypes.PounceOnMotion) #wait_for_completed(25)   #.wait_for_started(timeout=30)
    time.sleep(20)
    pounce.stop()
    robot.go_to_pose(pose).wait_for_completed()


def game():

    robot.say_text("I want to play a game!").wait_for_completed()

    # '''Quick Tap - tap your cube as fast as possible when the colors match, but never tap on red!
    #
    # The game ends when a player scores 5 points.
    # '''
    # import asyncio, random, sys, time
    #
    # import cozmo
    #
    # from cozmo.lights import blue_light, Color, green_light, Light, red_light, white_light, off_light
    # from cozmo.util import degrees, distance_mm, radians, speed_mmps
    #
    # purple_light = Light(Color(name = 'purple', rgb = (255, 0, 255)))
    # yellow_light = Light(Color(name = 'yellow', rgb = (255, 255, 0)))
    #
    # LIGHT_COLORS_LIST = [blue_light, green_light, purple_light, red_light, white_light, yellow_light]
    #
    # CHOOSE_CUBES_STATE = 'choose_cubes' # If the game is in CHOOSE_CUBES_STATE, on_cube_tap assigns the player's cube.
    # GAME_STATE = 'game' # If the game is in GAME_STATE, on_cube_tap registers the tap time of the players.
    #
    # MAKE_BUZZERS_DIFFERENT_COLORS = 'MAKE_BUZZERS_DIFFERENT_COLORS'
    # MAKE_BUZZERS_RED = 'MAKE_BUZZERS_RED'
    # MAKE_BUZZERS_SAME_COLORS = 'MAKE_BUZZERS_SAME_COLORS'
    #
    # # The buzzers have a 50% chance of displaying the same colors.
    # RATE_MAKE_BUZZERS_DIFFERENT_COLORS = 0.17 # The buzzers have a 17% chance of displaying different colors.
    # RATE_MAKE_BUZZERS_RED = 0.33 # the buzzers have a 33% chance of displaying red.
    #
    # RATE_COZMO_ACCURACY = 0.9 # Cozmo has a 90% chance of reacting correctly to the buzzers.
    # # This number can therefore be lowered to have Cozmo more frequently make the wrong move.
    #
    # SCORE_TO_WIN = 5 # the game ends once either player's score has reached SCORE_TO_WIN
    #
    # class QuickTapGame:
    #     '''The game logic of Quick Tap.'''
    #     def __init__(self, robot: cozmo.robot.Robot):
    #         self.robot = robot
    #         robot.world.connect_to_cubes()
    #         self.player = QuickTapPlayer()
    #         self.cozmo_player = CozmoQuickTapPlayer(robot)
    #         robot.add_event_handler(cozmo.anim.EvtAnimationCompleted, self.on_anim_completed)
    #         robot.add_event_handler(cozmo.objects.EvtObjectTapped, self.on_cube_tap)
    #
    #         self.cubes = None
    #         self.countdown_cube = None
    #
    #         self.buzzer_display_type = None
    #
    #         self.round_start_time = time.time()
    #         self.quick_tap_player_1 = None
    #         self.quick_tap_player_2 = None
    #         self.round_over = False
    #
    #         self.quick_tap_state = CHOOSE_CUBES_STATE
    #
    #     async def move_cozmo_to_ready_pose(self):
    #         self.robot.set_lift_height(0, in_parallel = True)
    #         self.robot.set_head_angle(degrees(0), in_parallel = True)
    #         await self.robot.wait_for_all_actions_completed()
    #
    #     async def run(self):
    #         '''Assigns the cubes, then starts a new round until a player has won.'''
    #         await self.move_cozmo_to_ready_pose()
    #         self.print_starting_instructions()
    #         if not self.cubes_connected():
    #             print('Cubes did not connect successfully - check that they are nearby. You may need to replace the batteries.')
    #             return
    #         await self.assign_cubes()
    #         self.quick_tap_state = GAME_STATE
    #         while max(self.player.score, self.cozmo_player.score) < SCORE_TO_WIN:
    #             await self.game_round()
    #         await self.report_winner()
    #
    #     async def game_round(self):
    #         '''Sets up and runs a round of the game.
    #
    #         In run(), a new round starts unless a player's score reaches SCORE_TO_WIN.
    #
    #         First we ready the players and cubes, and then start the countdown.
    #         After the countdown, the cubes light up.  Then Cozmo makes his move.
    #         Once Cozmo's move is over, we determine the winner of the round,
    #         and Cozmo reacts accordingly.
    #         '''
    #         self.round_over = False
    #         await self.reset_players()
    #         await self.countdown_cube.countdown()
    #         await self.set_round_lights()
    #         self.round_start_time = time.time()
    #         await self.cozmo_player.determine_move(self.buzzer_display_type)
    #         while not self.round_over: # self.round_over is True when Cozmo's tap animation is completed
    #             await asyncio.sleep(0)
    #         await self.cozmo_anim_reaction()
    #
    #     async def set_round_lights(self):
    #         '''Waits a random delay, then sets a display on the buzzer cubes.'''
    #         await self.cube_light_delay()
    #         self.determine_buzzer_display()
    #         self.set_buzzer_lights()
    #
    #     async def reset_players(self):
    #         '''Gets the players and cubes ready for a new round.'''
    #         self.player.reset()
    #         self.cozmo_player.reset()
    #         await self.robot.set_lift_height(1.0).wait_for_completed()
    #         self.turn_off_buzzer_cubes()
    #
    #     async def cube_light_delay(self):
    #         '''Waits between 0 and 2 seconds.'''
    #         delay = random.random() * 2
    #         await asyncio.sleep(delay)
    #
    #     def determine_buzzer_display(self):
    #         '''Chooses a buzzer display type based on the probabilities defined above.'''
    #         probability_red = random.random()
    #         if probability_red < RATE_MAKE_BUZZERS_RED:
    #             self.buzzer_display_type = MAKE_BUZZERS_RED
    #         else:
    #             probability_different_colors = random.random()
    #             if probability_different_colors < RATE_MAKE_BUZZERS_DIFFERENT_COLORS:
    #                 self.buzzer_display_type = MAKE_BUZZERS_DIFFERENT_COLORS
    #             else:
    #                 self.buzzer_display_type = MAKE_BUZZERS_SAME_COLORS
    #
    #     def on_cube_tap(self, evt, obj, **kwargs):
    #         '''Responds to cube taps depending on quick_tap_state.
    #
    #         If in CHOOSE_CUBES_STATE, on_cube_tap assigns the player's cube.
    #         If in GAME_STATE, on_cube_tap registers the tap time of the players.
    #         '''
    #         if obj.object_id is not None:
    #             if self.quick_tap_state == CHOOSE_CUBES_STATE:
    #                 if self.cozmo_player.cube is None:
    #                     # Cozmo hasn't picked a cube yet - ignore
    #                     pass
    #                 elif obj.object_id != self.cozmo_player.cube.object_id:
    #                     self.player.cube = obj
    #                     self.player.cube.set_lights_off()
    #             elif self.quick_tap_state == GAME_STATE:
    #                 self.turn_off_buzzer_cubes()
    #                 if obj.object_id == self.player.cube.object_id:
    #                     self.player.register_tap(self.round_start_time)
    #                 elif obj.object_id == self.cozmo_player.cube.object_id:
    #                     self.cozmo_player.register_tap(self.round_start_time)
    #
    #     async def on_anim_completed(self, evt, animation_name, **kwargs):
    #         '''Signals the end of the round if the animation completed was Cozmo's tap animation.'''
    #         if self.quick_tap_state == GAME_STATE and animation_name in ['OnSpeedtapTap', 'OnSpeedtapFakeout', 'OnSpeedtapIdle']:
    #             await self.determine_result_of_round()
    #             self.round_over = True
    #
    #     async def determine_result_of_round(self):
    #         '''Determines the first tapper, then whether that tapper wins or loses based on the buzzer display.'''
    #         self.determine_first_tapper()
    #         if self.quick_tap_player_1:
    #             if self.buzzer_display_type == MAKE_BUZZERS_SAME_COLORS:
    #                 self.quick_tap_player_1.wins_round()
    #                 await self.quick_tap_player_1.cube.flair_correct_tap()
    #             elif self.buzzer_display_type == MAKE_BUZZERS_DIFFERENT_COLORS or self.buzzer_display_type == MAKE_BUZZERS_RED:
    #                 self.quick_tap_player_2.wins_round()
    #                 await self.quick_tap_player_1.cube.flair_incorrect_tap()
    #             self.report_scores()
    #
    #     def determine_first_tapper(self):
    #         '''Finds the first tapper from the players' registered tap times.'''
    #         if self.player.has_tapped or self.cozmo_player.has_tapped:
    #             if self.cozmo_player.elapsed_tap_time < self.player.elapsed_tap_time:
    #                 self.quick_tap_player_1 = self.cozmo_player
    #                 self.quick_tap_player_2 = self.player
    #             else:
    #                 self.quick_tap_player_1 = self.player
    #                 self.quick_tap_player_2 = self.cozmo_player
    #         else:
    #             self.quick_tap_player_1 = None
    #
    #     async def cozmo_anim_reaction(self):
    #         '''Cozmo plays an animation based on whether he won or lost the round.'''
    #         if self.cozmo_player.won_round:
    #             await self.robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapHandCozmoWin).wait_for_completed()
    #         else:
    #             await self.robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapHandPlayerWin).wait_for_completed()
    #
    #     async def assign_cubes(self):
    #         '''Cozmo chooses his cube, then the player chooses,
    #         and the remaining cube becomes the countdown cube.
    #         '''
    #         await self.cozmo_player.select_cube()
    #         self.blink_available_cubes()
    #         await self.robot.world.wait_for(cozmo.objects.EvtObjectTapped)
    #         self.player.cube.stop_light_chaser()
    #         self.assign_countdown_cube()
    #
    #     def blink_available_cubes(self):
    #         '''Blinks the cubes which Cozmo did not select for himself.'''
    #         for cube in self.cubes:
    #             if cube.object_id != self.cozmo_player.cube.object_id:
    #                 cube.start_light_chaser(0.5)
    #
    #     def assign_countdown_cube(self):
    #         '''Assigns the countdown cube to be whichever cube has not been selected by the player or Cozmo.'''
    #         for cube in self.cubes:
    #             if cube.object_id != self.cozmo_player.cube.object_id and cube.object_id != self.player.cube.object_id:
    #                 self.countdown_cube = cube
    #                 self.countdown_cube.stop_light_chaser()
    #
    #     def set_buzzer_lights(self):
    #         '''Sets the buzzer cube lights based on the buzzer display type.'''
    #         if self.buzzer_display_type == MAKE_BUZZERS_RED:
    #             self.turn_on_buzzer_cubes_red()
    #         elif self.buzzer_display_type == MAKE_BUZZERS_DIFFERENT_COLORS:
    #             self.turn_on_buzzer_cubes_different()
    #         elif self.buzzer_display_type == MAKE_BUZZERS_SAME_COLORS:
    #             self.turn_on_buzzer_cubes_same()
    #
    #     def turn_on_buzzer_cubes_same(self):
    #         '''Sets the buzzer cubes to the same randomly generated color pair.'''
    #         same_colors = self.generate_random_buzzer_colors()
    #         self.player.cube.set_light_corners(*same_colors)
    #         self.cozmo_player.cube.set_light_corners(*same_colors)
    #
    #     def turn_on_buzzer_cubes_different(self):
    #         '''Sets the buzzer cubes to different randomly generated color pairs.'''
    #         player_cube_colors = self.generate_random_buzzer_colors()
    #         cozmo_cube_colors = self.generate_random_buzzer_colors()
    #         while player_cube_colors == cozmo_cube_colors:
    #             cozmo_cube_colors = self.generate_random_buzzer_colors()
    #         self.player.cube.set_light_corners(*player_cube_colors)
    #         self.cozmo_player.cube.set_light_corners(*cozmo_cube_colors)
    #
    #     def turn_on_buzzer_cubes_red(self):
    #         '''Sets the buzzer cubes to red.'''
    #         self.player.cube.set_lights(cozmo.lights.red_light)
    #         self.cozmo_player.cube.set_lights(cozmo.lights.red_light)
    #
    #     def generate_random_buzzer_colors(self):
    #         '''Creates a list of different alternating colors, chosen randomly from LIGHT_COLORS_LIST.
    #
    #         Returns:
    #             a list of Lights from LIGHT_COLORS_LIST
    #         '''
    #         num_colors = len(LIGHT_COLORS_LIST)
    #         x = random.randrange(num_colors)
    #         y = random.randrange(num_colors)
    #         while y == x:
    #             y = random.randrange(num_colors)
    #         return [LIGHT_COLORS_LIST[x], LIGHT_COLORS_LIST[y], LIGHT_COLORS_LIST[x], LIGHT_COLORS_LIST[y]]
    #
    #     def turn_off_buzzer_cubes(self):
    #         '''Turns off both buzzer cubes' lights.'''
    #         self.player.cube.set_lights_off()
    #         self.cozmo_player.cube.set_lights_off()
    #
    #     def cubes_connected(self):
    #         '''Checks if Cozmo connects to all three cubes successfully.
    #
    #         Returns:
    #             bool specifying if all three cubes have been successfully connected'''
    #         cube1 = self.robot.world.get_light_cube(cozmo.objects.LightCube1Id)
    #         cube2 = self.robot.world.get_light_cube(cozmo.objects.LightCube2Id)
    #         cube3 = self.robot.world.get_light_cube(cozmo.objects.LightCube3Id)
    #         self.cubes = [cube1, cube2, cube3]
    #         return not (cube1 == None or cube2 == None or cube3 == None)
    #
    #     def print_starting_instructions(self):
    #         print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    #         print('Welcome to Quick Tap!')
    #         print('Put 1 cube in front of Cozmo. It will turn white when he can see it.')
    #         print('Cozmo will tap the cube to select it as his buzzer.')
    #         print('After Cozmo, tap a cube to select your buzzer.')
    #         print('The last cube will display a countdown with its lights start each round.')
    #         print('When the buzzers light up, tap if the colors match, but never tap on red!')
    #         print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    #
    #     def report_scores(self):
    #         '''Prints the current scores of the game.'''
    #         print('---------------------------------------------------')
    #         print('Player score: {}'.format(self.player.score))
    #         print('Cozmo score: {}'.format(self.cozmo_player.score))
    #         print('---------------------------------------------------')
    #
    #     async def report_winner(self):
    #         '''Prints the final scores of the game, and the winner.'''
    #         print('You won {} round{}'.format(self.player.score, 's' if self.player.score != 1 else ''))
    #         print('Cozmo won {} round{}'.format(self.cozmo_player.score, 's' if self.cozmo_player.score != 1 else ''))
    #         if self.cozmo_player.score > self.player.score:
    #             print('~COZMO WINS QUICK TAP~')
    #             await self.robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapGameCozmoWinHighIntensity).wait_for_completed()
    #         else:
    #             print('~PLAYER WINS QUICK TAP~')
    #             await self.robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapGamePlayerWinHighIntensity).wait_for_completed()
    #
    #
    # class QuickTapPlayer():
    #     '''Player-specifc Quick Tap logic.'''
    #     def __init__(self):
    #         self.cube = None
    #         self.score = 0
    #         self.has_tapped = False
    #         self.name = 'Player'
    #         self.elapsed_tap_time = None
    #         self.won_round = False
    #
    #     def wins_round(self):
    #         '''Prints winning message, updates score, and sets won_round flag to True.'''
    #         print('****{} wins the round****'.format(self.name))
    #         self.score += 1
    #         self.won_round = True
    #
    #     def reset(self):
    #         '''Resets elapsed_tap_time, and sets has_tapped and won_round flags to False.'''
    #         self.elapsed_tap_time = sys.maxsize
    #         self.has_tapped = False
    #         self.won_round = False
    #
    #     def register_tap(self, round_start_time):
    #         '''Calculates elapsed time of tap, and sets has_tapped flag to True.
    #
    #         Args:
    #             round_start_time (Time): time stamp set in QuickTapGame to calculate players' elapsed_tap_time
    #         '''
    #         self.elapsed_tap_time = time.time() - round_start_time
    #         self.has_tapped = True
    #
    #
    # class CozmoQuickTapPlayer(QuickTapPlayer):
    #     '''Cozmo-specific Quick Tap player logic, with a reference to the actual Cozmo robot.
    #
    #     Args:
    #         robot (cozmo.robot.Robot): passed in from the QuickTapGame class
    #     '''
    #     def __init__(self, robot: cozmo.robot.Robot):
    #         super().__init__()
    #         self.robot = robot
    #         self.name = 'Cozmo'
    #
    #     async def select_cube(self):
    #         '''Cozmo looks for a cube, drives to it, and taps it.'''
    #         self.cube = await self.robot.world.wait_for_observed_light_cube()
    #         self.cube.set_lights(cozmo.lights.white_light)
    #         await asyncio.sleep(2)
    #         self.cube.start_light_chaser(0.5)
    #         await self.robot.set_lift_height(1.0).wait_for_completed()
    #         await self.robot.go_to_object(self.cube, distance_mm(40)).wait_for_completed()
    #         await self.robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapTap).wait_for_completed()
    #         self.cube.stop_light_chaser()
    #         self.cube.set_lights(green_light)
    #
    #     async def determine_move(self, buzzer_display_type):
    #         '''Cozmo chooses a move based on the probabilities above.
    #
    #         Args:
    #             buzzer_display_type (string): the display of the buzzers
    #             Either MAKE_BUZZERS_DIFFERENT_COLORS, MAKE_BUZZERS_RED, or MAKE_BUZZERS_SAME_COLORS
    #         '''
    #         await self.hesitate()
    #         probability_correct = random.random()
    #         if probability_correct < RATE_COZMO_ACCURACY:
    #             if buzzer_display_type == MAKE_BUZZERS_SAME_COLORS:
    #                 await self.tap()
    #             else:
    #                 await self.fail_to_tap()
    #         else:
    #             if buzzer_display_type == MAKE_BUZZERS_RED or buzzer_display_type == MAKE_BUZZERS_DIFFERENT_COLORS:
    #                 await self.tap()
    #             else:
    #                 await self.fail_to_tap()
    #
    #     async def hesitate(self):
    #         '''Cozmo waits between 0 and 0.5 seconds'''
    #         delay = random.random() * .5
    #         await asyncio.sleep(delay)
    #
    #     async def tap(self):
    #         '''Calls Cozmo's tap animation.'''
    #         await self.robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapTap).wait_for_completed()
    #
    #     async def fail_to_tap(self):
    #         '''Randomly calls either Cozmo's fakeout tap animation or his idle animation.'''
    #         probability_fakeout = random.random()
    #         if probability_fakeout < 0.5:
    #             await self.robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapFakeout).wait_for_completed()
    #         else:
    #             await self.robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapIdle).wait_for_completed()
    #
    #
    # rainbow_colors = [blue_light, red_light, green_light, yellow_light]
    #
    # class BlinkyCube(cozmo.objects.LightCube):
    #     '''Same as a normal cube, plus extra methods specific to Quick Tap.'''
    #     def __init__(self, *a, **kw):
    #         super().__init__(*a, **kw)
    #         self._chaser = None
    #
    #     def start_light_chaser(self, pause_time):
    #         '''Rotates four colors around the cube light corners in a continuous loop.
    #
    #         Args:
    #             pause_time (float): the time awaited before moving the rotating lights
    #         '''
    #         if self._chaser:
    #             raise ValueError('Light chaser already running')
    #         async def _chaser():
    #             while True:
    #                 for i in range(4):
    #                     self.set_light_corners(*rainbow_colors)
    #                     await asyncio.sleep(pause_time, loop = self._loop)
    #                     light = rainbow_colors.pop(0)
    #                     rainbow_colors.append(light)
    #         self._chaser = asyncio.ensure_future(_chaser(), loop = self._loop)
    #
    #     def stop_light_chaser(self):
    #         '''Ends the _chaser loop.'''
    #         if self._chaser:
    #             self._chaser.cancel()
    #             self._chaser = None
    #         self.set_lights_off()
    #
    #     async def countdown(self):
    #         '''Sets all lights to white, then 3 lights, then 2 lights, then 1 light, then none.'''
    #         for i in range(5):
    #             cols = [white_light] * (4 - i) + [off_light] * i
    #             self.set_light_corners(*cols)
    #             await asyncio.sleep(.5)
    #
    #     async def flair_correct_tap(self):
    #         '''Runs a fast _chaser when the player taps correctly.'''
    #         self.start_light_chaser(0.1)
    #         await asyncio.sleep(2)
    #         self.stop_light_chaser()
    #
    #     async def flair_incorrect_tap(self):
    #         '''Blinks red when the player taps incorrectly.'''
    #         for _ in range(4):
    #             self.set_lights(red_light)
    #             await asyncio.sleep(.2)
    #             self.set_lights(off_light)
    #             await asyncio.sleep(.2)
    #
    #
    # # Make sure World knows how to instantiate the BlinkyCube subclass
    # cozmo.world.World.light_cube_factory = BlinkyCube
    #
    # async def cozmo_program(robot: cozmo.robot.Robot):
    #     game = QuickTapGame(robot)
    #     await game.run()
    #
    # cozmo.run_program(cozmo_program)


def action14_shortbricks(robot: cozmo.robot.Robot):
    pose = robot.pose
    robot.world.connect_to_cubes() ##################### needed? I added in
    random_selection = random.randint(1, 2)
    robot.say_text("Help me find my cubes!").wait_for_completed()

    # #roll block
    if random_selection == 1:
        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cube = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=30)
        print("Found %s cubes" % len(cube))
        lookaround.stop()

        if len(cube) == 0:
            robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail).wait_for_completed()
        else:
            robot.run_timed_behavior(cozmo.behavior.BehaviorTypes.RollBlock, active_time=60)


    # do a wheelie
    if random_selection == 2:

        cube = None
        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        # print(cube)
        print("Hello1")
        # print("Found %s cubes" % len(cube))
        lookaround.stop()
        print("Hello2")

        # if len(cube) == 0:
        if cube is None:
            print("Hello3")
            # robot.play_anim_trigger(cozmo.anim.Triggers.Majorfail).wait_for_completed()
        else:
            action = robot.pop_a_wheelie(cube, num_retries=2)
            action.wait_for_completed()

    robot.world.disconnect_from_cubes()
    robot.go_to_pose(pose).wait_for_completed()


def action15_longbricks(robot: cozmo.robot.Robot):
    robot.say_text("Help me find my cubes!").wait_for_completed()
    pose = robot.pose
    robot.world.connect_to_cubes()
    # Attempt to stack 2 cubes

    # Lookaround until Cozmo knows where at least 2 cubes are:
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()

    if len(cubes) < 2:
        print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
    else:
        # Try and pickup the 1st cube
        current_action = robot.pickup_object(cubes[0], num_retries=3)
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

        # Now try to place that cube on the 2nd one
        current_action = robot.place_on_object(cubes[1], num_retries=3)
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            print("Place On Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

        print("Cozmo successfully stacked 2 blocks!")

        robot.start_behavior(cozmo.behavior.BehaviorTypes.KnockOverCubes).wait_for_completed()

    robot.world.disconnect_from_cubes()
    robot.go_to_pose(pose).wait_for_completed()

def action16_background(robot: cozmo.robot.Robot):

    pose = robot.pose

    robot.set_head_angle(degrees(45), duration =1.5).wait_for_completed()
    robot.set_lift_height(height=1, duration=1.5).wait_for_completed()
    robot.turn_in_place(degrees(360)).wait_for_completed()
    robot.set_head_angle(degrees(0), duration =1.5).wait_for_completed()
    robot.set_lift_height(height=0, duration=1.5).wait_for_completed()

    for _ in range(4):
        robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()


    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    time.sleep(20)
    # cubes = robot.world.wait_until_observe_num_objects(num=4, object_type=cozmo.objects.LightCube, timeout=20)
    lookaround.stop()

    robot.go_to_pose(pose).wait_for_completed()

def action17_charger(robot: cozmo.robot.Robot):
    robot.say_text("Put me on the charger!").wait_for_completed()
    # from cozmo.util import degrees, distance_mm, radians, speed_mmps
    # import time
    # import math
    #
    # def find_charger():
    #     # global robot
    #
    #     while(True):
    #
    #         behavior = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    #         try:
    #             seen_charger = robot.world.wait_for_observed_charger(timeout=10,include_existing=True)
    #         except:
    #             seen_charger = None
    #         behavior.stop()
    #         if(seen_charger != None):
    #             #print(seen_charger)
    #             return seen_charger
    #         # frustrated(robot)
    #         robot.say_text('Charge?',duration_scalar=0.5).wait_for_completed()
    #     return None
    #
    # def go_to_charger():
    #     # Driving towards charger without much precision
    #     # global robot
    #
    #     charger = None
    #     ''' cf. 08_drive_to_charger_test.py '''
    #     # see if Cozmo already knows where the charger is
    #     if robot.world.charger:
    #         # make sure Cozmo was not delocalised after observing the charger
    #         if robot.world.charger.pose.is_comparable(robot.pose):
    #             print("Cozmo already knows where the charger is!")
    #             charger = robot.world.charger
    #         else:
    #             # Cozmo knows about the charger, but the pose is not based on the
    #             # same origin as the robot (e.g. the robot was moved since seeing
    #             # the charger) so try to look for the charger first
    #             pass
    #     if not charger:
    #         charger = find_charger()
    #
    #     action = robot.go_to_object(charger,distance_from_object=distance_mm(80), in_parallel=False, num_retries=5)
    #     #action = robot.go_to_pose(charger.pose)
    #     action.wait_for_completed()
    #     return charger
    #
    # def disp_coord(charger: cozmo.objects.Charger):
    #     # Debugging function used to diplay coordinates of objects
    #     # (Not currently used)
    #     # global robot
    #
    #     r_coord = robot.pose.position #.x .y .z, .rotation otherwise
    #     r_zRot = robot.pose_angle.degrees # or .radians
    #     c_coord = charger.pose.position
    #     c_zRot = charger.pose.rotation.angle_z.degrees
    #
    #     print('Recorded coordinates of the robot and charger:')
    #     print('Robot: ',end=' ')
    #     print(r_coord)
    #     print(r_zRot)
    #     print('Charger: ',end=' ')
    #     print(c_coord)
    #     print(c_zRot)
    #     print('\n')
    #
    # PI = 3.14159265359
    # def clip_angle(angle=3.1415):
    # 	# Allow Cozmo to turn the least possible. Without it, Cozmo could
    # 	# spin on itself several times or turn for instance -350 degrees
    # 	# instead of 10 degrees.
    #     # global PI
    #
    #     # Retreive supplementary turns (in radians)
    #     while(angle >= 2*PI):
    #         angle -= 2*PI
    #     while(angle <= -2*PI):
    #         angle += 2*PI
    #     # Select shortest rotation to reach the target
    #     if(angle > PI):
    #     	angle -= 2*PI
    #     elif(angle < -PI):
    #     	angle += 2*PI
    #     return angle
    #
    # def check_tol(charger: cozmo.objects.Charger,dist_charger=40):
    #     # Check if the position tolerance in front of the charger is respected
    #     # global robot,PI
    #
    #     distance_tol = 5 # mm, tolerance for placement error
    #     angle_tol = 5*PI/180 # rad, tolerance for orientation error
    #
    #     try:
    #         charger = robot.world.wait_for_observed_charger(timeout=2,include_existing=True)
    #     except:
    #         print('WARNING: Cannot see the charger to verify the position.')
    #
    #     # Calculate positions
    #     r_coord = [0,0,0]
    #     c_coord = [0,0,0]
    #     # Coordonates of robot and charger
    #     r_coord[0] = robot.pose.position.x #.x .y .z, .rotation otherwise
    #     r_coord[1] = robot.pose.position.y
    #     r_coord[2] = robot.pose.position.z
    #     r_zRot = robot.pose_angle.radians # .degrees or .radians
    #     c_coord[0] = charger.pose.position.x
    #     c_coord[1] = charger.pose.position.y
    #     c_coord[2] = charger.pose.position.z
    #     c_zRot = charger.pose.rotation.angle_z.radians
    #
    #     # Create target position
    #     # dist_charger in mm, distance if front of charger
    #     c_coord[0] -=  dist_charger*math.cos(c_zRot)
    #     c_coord[1] -=  dist_charger*math.sin(c_zRot)
    #
    #     # Direction and distance to target position (in front of charger)
    #     distance = math.sqrt((c_coord[0]-r_coord[0])**2 + (c_coord[1]-r_coord[1])**2 + (c_coord[2]-r_coord[2])**2)
    #
    #     if(distance < distance_tol and math.fabs(r_zRot-c_zRot) < angle_tol):
    #     	return 1
    #     else:
    #     	return 0
    #
    # def final_adjust(charger: cozmo.objects.Charger,dist_charger=40,speed=20,critical=False):
    #     # Final adjustement to properly face the charger.
    #     # The position can be adjusted several times if
    #     # the precision is critical, i.e. when climbing
    #     # back onto the charger.
    #     # global robot,PI
    #
    #     while(True):
    #         # Calculate positions
    # 	    r_coord = [0,0,0]
    # 	    c_coord = [0,0,0]
    # 	    # Coordonates of robot and charger
    # 	    r_coord[0] = robot.pose.position.x #.x .y .z, .rotation otherwise
    # 	    r_coord[1] = robot.pose.position.y
    # 	    r_coord[2] = robot.pose.position.z
    # 	    r_zRot = robot.pose_angle.radians # .degrees or .radians
    # 	    c_coord[0] = charger.pose.position.x
    # 	    c_coord[1] = charger.pose.position.y
    # 	    c_coord[2] = charger.pose.position.z
    # 	    c_zRot = charger.pose.rotation.angle_z.radians
    #
    # 	    # Create target position
    # 	    # dist_charger in mm, distance if front of charger
    # 	    c_coord[0] -=  dist_charger*math.cos(c_zRot)
    # 	    c_coord[1] -=  dist_charger*math.sin(c_zRot)
    #
    # 	    # Direction and distance to target position (in front of charger)
    # 	    distance = math.sqrt((c_coord[0]-r_coord[0])**2 + (c_coord[1]-r_coord[1])**2 + (c_coord[2]-r_coord[2])**2)
    # 	    vect = [c_coord[0]-r_coord[0],c_coord[1]-r_coord[1],c_coord[2]-r_coord[2]]
    # 	    # Angle of vector going from robot's origin to target's position
    # 	    theta_t = math.atan2(vect[1],vect[0])
    #
    # 	    print('CHECK: Adjusting position')
    # 	    # Face the target position
    # 	    angle = clip_angle((theta_t-r_zRot))
    # 	    robot.turn_in_place(radians(angle)).wait_for_completed()
    # 	    # Drive toward the target position
    # 	    robot.drive_straight(distance_mm(distance),speed_mmps(speed)).wait_for_completed()
    # 	    # Face the charger
    # 	    angle = clip_angle((c_zRot-theta_t))
    # 	    robot.turn_in_place(radians(angle)).wait_for_completed()
    #
    #         # In case the robot does not need to climb onto the charger
    # 	    if not critical:
    # 	        break
    # 	    elif(check_tol(charger,dist_charger)):
    # 	    	print('CHECK: Robot aligned relativ to the charger.')
    # 	    	break
    #     return
    #
    # def restart_procedure(charger: cozmo.objects.Charger):
    #     # global robot
    #
    #     robot.stop_all_motors()
    #     robot.set_lift_height(height=0.5,max_speed=10,in_parallel=True).wait_for_completed()
    #     robot.pose.invalidate()
    #     charger.pose.invalidate()
    #     print('ABORT: Driving away')
    #     #robot.drive_straight(distance_mm(150),speed_mmps(80),in_parallel=False).wait_for_completed()
    #     robot.drive_wheels(80,80,duration=2)
    #     turn_around()
    #     robot.set_lift_height(height=0,max_speed=10,in_parallel=True).wait_for_completed()
    #     # Restart procedure
    #     get_on_charger()
    #     return
    #
    # def get_on_charger():
    #     # global robot,pitch_threshold
    #
    #     robot.set_head_angle(degrees(0),in_parallel=False).wait_for_completed()
    #     pitch_threshold = math.fabs(robot.pose_pitch.degrees)
    #     pitch_threshold += 1 # Add 1 degree to threshold
    #     print('Pitch threshold: ' + str(pitch_threshold))
    #
    #     # Drive towards charger
    #     go_to_charger()
    #
    #     # Let Cozmo first look for the charger once again. The coordinates
    #     # tend to be too unprecise if an old coordinate system is kept.
    #     if robot.world.charger is not None and robot.world.charger.pose.is_comparable(robot.pose):
    #         robot.world.charger.pose.invalidate()
    #     charger = find_charger()
    #
    #     # Adjust position in front of the charger
    #     final_adjust(charger,critical=True)
    #
    #     # Turn around and start going backward
    #     turn_around()
    #     robot.drive_wheel_motors(-120,-120)
    #     robot.set_lift_height(height=0.5,max_speed=10,in_parallel=True).wait_for_completed()
    #     robot.set_head_angle(degrees(0),in_parallel=True).wait_for_completed()
    #
    #     # This section allow to wait for Cozmo to arrive on its charger
    #     # and detect eventual errors. The whole procedure will be restarted
    #     # in case something goes wrong.
    #     timeout = 1 # seconds before timeout
    #     t = 0
    #     # Wait for back wheels to climb on charger
    #     while(True):
    #         time.sleep(.1)
    #         t += 0.1
    #         if(t >= timeout):
    #             print('ERROR: robot timed out before climbing on charger.')
    #             restart_procedure(charger)
    #             return
    #         elif(math.fabs(robot.pose_pitch.degrees) >= pitch_threshold):
    #             print('CHECK: backwheels on charger.')
    #             break
    #     # Wait for front wheels to climb on charger
    #     timeout = 2
    #     t = 0
    #     while(True):
    #         time.sleep(.1)
    #         t += 0.1
    #         if(math.fabs(robot.pose_pitch.degrees) > 20 or t >= timeout):
    #             # The robot is climbing on charger's wall -> restart
    #             print('ERROR: robot climbed on charger\'s wall or timed out.')
    #             restart_procedure(charger)
    #             return
    #         elif(math.fabs(robot.pose_pitch.degrees) < pitch_threshold):
    #             print('CHECK: robot on charger, backing up on pins.')
    #             robot.stop_all_motors()
    #             break
    #
    #     # Final backup onto charger's contacts
    #     robot.set_lift_height(height=0,max_speed=10,in_parallel=True).wait_for_completed()
    #     robot.backup_onto_charger(max_drive_time=3)
    #     if(robot.is_on_charger):
    #         b = 0
    #         # while b == 0:
    #         battery = robot.battery_voltage
    #         print("Battery:", battery)
    #     	# print('PROCEDURE SUCCEEDED')
    #             # time.sleep(10)
    #             # print('PROCEDURE SUCCEEDED')
    #     else:
    #     	restart_procedure(charger)
    #     	return
    #
    #     # Celebrate success
    #     # robot.drive_off_charger_contacts().wait_for_completed()
    #     # celebrate(robot) # A small celebration where only the head moves
    #     # robot.backup_onto_charger(max_drive_time=3)
    #     return
    #
    # ########################## Battery related code ##########################
    #
    # def check_battery():
    # 	# global robot
    #
    # 	if(robot.battery_voltage < 3.5):
    # 		print('Battery is low, directly docking to charger without cleaning up.')
    # 		return 1
    # 	else:
    # 		return 0
    #
    # ########################## General code ##########################
    #
    # def turn_around():
    #     # global robot
    #     robot.turn_in_place(degrees(-178)).wait_for_completed()
    #     return
    #
    # def execute_procedure():
    #     low_battery = check_battery()
    #     # if not low_battery:
    #     #     clean_up_cubes()
    #     get_on_charger()
    #     return
    #
    # execute_procedure()


pub = rospy.Publisher('actiontime', Int8, queue_size=10)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

    if data.data == 1:
        cozmo.run_program(action1_happy)
        pub.publish(data.data)
        # rospy.loginfo('1')
    elif data.data == 2:
        cozmo.run_program(action2_sad)
        pub.publish(data.data)
        # rospy.loginfo('2')
    elif data.data == 3:
        cozmo.run_program(action3_angry)
        pub.publish(data.data)
        # rospy.loginfo('3')
    elif data.data == 4:
        cozmo.run_program(action4_shocked)
        pub.publish(data.data)
        # rospy.loginfo('4')
    elif data.data == 5:
        cozmo.run_program(action5_monster)
        pub.publish(data.data)
        # rospy.loginfo('5')
    elif data.data == 6:
        cozmo.run_program(action6_animal)
        pub.publish(data.data)
        # rospy.loginfo('6')
    elif data.data == 7:
        cozmo.run_program(action7_hyperactive)
        pub.publish(data.data)
        # rospy.loginfo('7')
    elif data.data == 8:
        cozmo.run_program(action8_ill)
        pub.publish(data.data)
        # rospy.loginfo('8')
    elif data.data == 9:
        cozmo.run_program(action9_song)
        pub.publish(data.data)
        # rospy.loginfo('9')
    elif data.data == 10:
        cozmo.run_program(action10_joke)
        pub.publish(data.data)
        # rospy.loginfo('10')
    elif data.data == 11:
        cozmo.run_program(action11_reminder)
        # rospy.loginfo('11')
    elif data.data == 12:
        cozmo.run_program(action12_handinteraction)
        pub.publish(data.data)
        # rospy.loginfo('12')
    elif data.data == 13:
        game()
        pub.publish(data.data)
        # cozmo.run_program(action13_game)
        # rospy.loginfo('13')
    elif data.data == 14:
        cozmo.run_program(action14_shortbricks)
        pub.publish(data.data)
        # rospy.loginfo('14')
    elif data.data == 15:
        cozmo.run_program(action15_longbricks)
        pub.publish(data.data)
        # rospy.loginfo('15')
    elif data.data == 16:
        cozmo.run_program(action16_background)
        pub.publish(data.data)
            # rospy.loginfo('16')
    elif data.data == 17:
        cozmo.run_program(action17_charger)
        pub.publish(data.data)
        # rospy.loginfo('17')


    # data.data will give the number of the enum
    # cozmo.run_program(cozmo_program)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', Int8, callback)
    # pub = rospy.Publisher('actiontime', Int8, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def cozmo_app(coz_conn):
    """
    The main function of the cozmo ROS driver.
    This function is called by cozmo SDK!
    Use "cozmo.connect(cozmo_app)" to run.
    :type   coz_conn:   cozmo.Connection
    :param  coz_conn:   The connection handle to cozmo robot.
    """
    coz = coz_conn.wait_for_robot()
    # coz.camera.image_stream_enabled = True
    # coz_ros = CozmoRos(coz)
    coz_ros.run()




if __name__ == '__main__':
    listener()
    rospy.init_node('cozmo_driver')
    cozmo.setup_basic_logging()
    try:
        cozmo.connect(cozmo_app)
    except cozmo.ConnectionError as e:
        sys.exit('A connection error occurred: {}'.format(e))
