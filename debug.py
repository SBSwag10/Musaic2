import time
import streamlit as st
import datetime
import pandas as pd  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

st.title("Musaic")

# Add your analysis logic here (replace with your code from analyze.py)
def truncate(string_list):
    string_list[:] = [string[:string.rfind('(')-1] for string in string_list]

def musaic_it():
  # Replace 'https://www.example.com' with the actual URL of the webpage
  options = webdriver.ChromeOptions()
  options.add_argument('--pageLoadStrategy=eager')  # Set pageLoadStrategy to eager

  driver = webdriver.Chrome(options=options)

  driver.get("https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D")

  # This finds the first element with the specified id or class
  # You'll need to replace 'element_id' or 'element_class' with the actual identifier of your target element
  results = driver.find_element(By.ID, "grid-container")  # Or By.CLASS_NAME, "element_class"
  topresult = results.find_element(By.ID, "thumbnail") 

  # Get the href attribute value
  href_value = topresult.get_attribute("href")
  vid_id = href_value[href_value.find("=")+1:]
  # print(vid_id)

  # driver.quit()

  # Set implicit wait time (in seconds)
  driver.implicitly_wait(10)

  url = "https://sonoteller.ai/"+vid_id
  driver.get(url)

  # Initial wait for main content (optional)
  initial_wait = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "page-content"))  # Replace with a suitable locator for your main content
  )

  # List of element locators (replace with your actual locators)
  element_locators = [
      (By.ID, "s-moods-l"),
      (By.ID, "s-themes"),
      (By.ID, "s-genres"),
      (By.ID, "s-styles"),
      (By.ID, "s-moods-m"),
      (By.ID, "s-instruments"),
      (By.ID, "s-bpm")
      # Add more locators for your elements
  ]

  elements = []
  for locator in element_locators:
    try:
      # Increased wait time per element (adjust as needed)
      element = WebDriverWait(driver, 5).until(
          EC.presence_of_element_located(locator)
      )
      if element.is_displayed():
        elements.append(element)
        print(f"Element with locator {locator} is visible.")
      else:
        print(f"Element with locator {locator} is not visible.")
    except:
      print(f"Failed to find element with locator {locator}.")


  lyric_mood_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-moods-l"))
  )
  lyric_mood_tags_all = lyric_mood_box.text
  lyric_mood_tags = lyric_mood_tags_all.split(", ")
  truncate(lyric_mood_tags)
  while len(lyric_mood_tags) == 1:
    lyric_mood_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-moods-l"))
  )
    lyric_mood_tags_all = lyric_mood_box.text
    lyric_mood_tags = lyric_mood_tags_all.split(", ")
    truncate(lyric_mood_tags)

  theme_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-themes"))
  )
  theme_tags_all = theme_box.text
  theme_tags = theme_tags_all.split(", ")
  truncate(theme_tags)
  while len(theme_tags) == 1:
    theme_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-themes"))
  )
    theme_tags_all = theme_box.text
    theme_tags = theme_tags_all.split(", ")
    truncate(theme_tags)
#change for commit
  genre_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-genres"))
  )
  genre_tags_all = genre_box.text
  genre_tags = genre_tags_all.split(", ")
  truncate(genre_tags)
  while len(genre_tags) == 1:
    genre_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-genres"))
  )
    genre_tags_all = genre_box.text
    genre_tags = genre_tags_all.split(", ")
    truncate(genre_tags)


  style_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-styles"))
  )
  style_tags_all = style_box.text
  style_tags = style_tags_all.split(", ")
  truncate(style_tags)
  while len(style_tags) == 1:
    style_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-styles"))
  )
    style_tags_all = style_box.text
    style_tags = style_tags_all.split(", ")
    truncate(style_tags)

  music_mood_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-moods-m"))
  )
  music_mood_tags_all = music_mood_box.text
  music_mood_tags = music_mood_tags_all.split(", ")
  truncate(music_mood_tags)
  while len(music_mood_tags) == 1:
    music_mood_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-moods-m"))
  )
    music_mood_tags_all = music_mood_box.text
    music_mood_tags = music_mood_tags_all.split(", ")
    truncate(music_mood_tags)


  instruments_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-instruments"))
  )
  instruments_all = instruments_box.text
  instruments = instruments_all.split(", ")
  while len(instruments) == 1:
    instruments_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-instruments"))
  )
    instruments_all = instruments_box.text
    instruments = instruments_all.split(", ")

  bpm_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-bpm"))
  )
  bpm = bpm_box.text
  while bpm == "":
    bpm_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "s-bpm"))
  )
    bpm = bpm_box.text
#new
  # print(lyric_mood_tags)
  # print(theme_tags)
  # print(genre_tags)
  # print(style_tags)
  # print(music_mood_tags)
  # print(instruments)
  # print(bpm)

  data = {
      "lyric_mood_tags": lyric_mood_tags,
      "theme_tags": theme_tags,
      "genre_tags": genre_tags,
      "style_tags": style_tags,
      "music_mood_tags": music_mood_tags,
      "instruments": instruments,
      "bpm": bpm
  }

  return data

# def samplesong():
#   song = ""

#   options = webdriver.ChromeOptions()
#   options.add_argument('--pageLoadStrategy=eager')  # Set pageLoadStrategy to eager

#   driver = webdriver.Chrome(options=options)

#   driver.get("https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D")

#   return song

def concat(list):
  tag_ready=""
  for i in range(len(list)-1):
    tag_ready = tag_ready + list[i] + ", "
  return tag_ready

today = datetime.date.today()

st.header("Analysis Results ("+today.strftime("%m/%d/%Y")+"):")
# print(data)

with st.spinner('Wait for it...'):
  time.sleep(10)

  data = musaic_it()
  mood = ""
  sep = ", "

  st.subheader("**Consumer Market Summary**")

  st.write("As of today, listeners seem to be responsive to music with themes centering on " + concat(data["theme_tags"]).lower() + "and " + data["theme_tags"][len(data["theme_tags"])-1].lower() + ".  Lyrically, consumers are likely to serially stream songs that convey" + concat(data["lyric_mood_tags"]).lower() + " and " + data["lyric_mood_tags"][len(data["lyric_mood_tags"])-1].lower() + ". These most-consumed hits fall under genres like "+ concat(data["genre_tags"]) + " and " + data["genre_tags"][len(data["genre_tags"])-1] + ", with "+ data["style_tags"][0] + " and " + data["style_tags"][1] +" styles being particularly prominent. These trends in the top hits also seem to suggest that incorporating "+data["instruments"][0].lower()+"s and " +data["instruments"][1]+" into songs that release within a time frame where this advice will remain applicable but changes in production can be made will receive strong commercial reception.")

  st.subheader("**Tag Words and Infometrics**")

  for i in data["lyric_mood_tags"]:
    if i==0:
      sep=" "
    mood = mood + sep + i
  mood=mood[1:]
  st.write("***Lyrical Mood***: "+mood)

  mood = ""
  for i in data["theme_tags"]:
    if i==0:
      sep=" "
    mood = mood + sep + i
  mood=mood[1:]
  st.write("***Themes***: "+mood)

  mood = ""
  for i in data["genre_tags"]:
    if i==0:
      sep=" "
    mood = mood + sep + i
  mood=mood[1:]
  st.write("***Genre***: "+mood)

  mood = ""
  for i in data["style_tags"]:
    if i==0:
      sep=" "
    mood = mood + sep + i
  mood=mood[1:]
  st.write("***Music Style***: "+mood)

  mood = ""
  for i in data["music_mood_tags"]:
    if i==0:
      sep=" "
    mood = mood + sep + i
  mood=mood[1:]
  st.write("***Music Mood***: "+mood)

  mood = ""
  for i in data["instruments"]:
    if i==0:
      sep=" "
    mood = mood + sep + i
  mood=mood[1:]
  st.write("***Instruments***: "+mood)

  mood = ""
  for i in data["bpm"]:
    sep=""
    mood = mood + sep + i
  st.write("***BPM***: "+mood)

  st.subheader("Downloadable DataFrame with Tag Words")

  df=pd.DataFrame.from_records(data,index=['1', '2', '3', '4', '5'])
  df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
  st.dataframe(df)

  st.subheader("**Next Steps**")

  st.subheader("Record Label/Management Executives")

  st.write("Record label and Management executives can utilize this report to find contracted artists who are currently creating singles or EPs that align with these findings and infometrics. Once these artists are identified, this report can be used as documentation to give them monetary incentives or aid in releasing the projects in time to capitalize on this sub-cycle of the consumer market. Effective use of this report could indirectly increase the potential profit of the company through many profit channels (i.e. artist royalties, sync license royalties, etc.). For any further action in parallel processes or protocol, forward this report to the necessary teams or departments for further action.")

  st.subheader("A&R Representatives, Talent Scouts, Marketing & PR Dept.")

  st.write("A&R reps and talent scouts can coordinate with the Marketing & PR Departments to efficiently find artists who have released music that can be described by the produced tag words and promote said releases. Similar actions to this could further corporate profit, through incentives for independent artists to sign with the firm and third-party vendor profit royalties. For further action utilizing the contents of this report, submit the information to your manager and the necessary personnel.")

  st.subheader("Artists, Songwriters, Producers, Sound Engineers, etc.")

  st.write("For music creators, this report can be made of use in many ways including the following: \n 1. A direct jump-off point for creating and releasing quick, commercial projects \n 2. Tag words can be input into AI music generators to aid in the creative process. If you have questions regarding legality of certain use cases with in the context of your employment, please contact your corporation's legal team prior to use.  ")

  st.subheader("Venue Vendors")

  st.write("Venue vendors can use this report to find artists that are making music similar to what the tag words describe, and correspondingly book them. This provides for a mutually beneficial turn of profits between both parties. To proceed further with this report in pursuit of this use case, make sure you are complying with your company's policies and the opposite party's record label and management firm policies before submitting a vendor-side contract offer for lease of venue")

  st.write("**NOTE: THESE USE CASES NEITHER RECOMMEND GOING AGAINST NOR SUPERCEDE CORPORATE POLICY OR CONTRACTUAL OBLIGATIONS, NOR DOES IT CONSTITUTE LEGAL ADVICE. If you have questions regarding legality of certain use cases within the context of your employment, please contact your corporation's legal team prior to use.**")

  # Replace 'your_song.mp3' with the path to your audio file (use forward slashes '/')
  # song_path = "Song.mp3"  # Assuming the song is in the same directory

  # def download_mp3():
  #   with open(song_path, "rb") as f:
  #     st.download_button(download_link_text, f.read(), file_name=song_path)

  # # Download link text (customize as desired)
  # download_link_text = "Download MP3"

  # # Display the download link
  # st.button(download_link_text, on_click=download_mp3)