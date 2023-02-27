import streamlit as st
from PIL import Image
st.title("Our Vast Universe")
image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\spaceman.jpg')
st.image(image, caption='A spaceman in the space', width=500)
st.subheader("The universe where light and darkness coexist is a space of creation where new things are made, and it is where unknown worlds beyond our imagination coexist. That’s why the pictures of the universe capture our hearts. What kind of place is the universe where there is eternal time and space?")
btn_click = st.button("Amazing fact!")
if btn_click == True:
    st.balloons()
    st.caption('Speed of our universe expansion is very fast than the speed of light. we think nothing can beat the speed of light :smile:')
else:
    st.write('you are missing an amazing fact:cry:')
option = st.selectbox(
    'select one to know about it.',
    ('Sun','Stephenson 2-18','Mercury', 'Venus', 'Mars' , 'Jupiter','Saturn', 'Uranus', 'Neptune'))
st.write('You selected:', option)
if option=='Sun':
    image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\sun.jpg')
    st.image(image)
    st.markdown("The Sun is the largest object in our solar system. The Sun’s volume would need 1.3 million Earths to fill it. Its gravity holds the solar system together, keeping everything from the biggest planets to the smallest bits of debris in orbit around it. The hottest part of the Sun is its core, where temperatures top 27 million degrees Fahrenheit (15 million degrees Celsius). The Sun’s activity, from its powerful eruptions to the steady stream of charged particles it sends out, influences the nature of space throughout the solar system.")
elif option=="Stephenson 2-18":
    image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\Stephenson_2-18.webp')
    st.image(image)
    st.markdown("Stephenson 2-18 is a red supergiant of the spectral type M6. It is one of the largest stars ever discovered, with a radius of 2,150 solar radii.The star’s size corresponds to a volume about 10 billion times greater than the Sun.")
elif option=="Mercury":
    image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\mercury.jpg')
    st.image(image)
    st.markdown(" Mercury is hot, but not too hot for ice.""\nThe closest planet to the Sun does indeed have ice on its surface. That sounds surprising at first glance, but the ice is found in permanently shadowed craters — those that never receive any sunlight. It is thought that perhaps comets delivered this ice to Mercury in the first place. In fact, NASA’s MESSENGER spacecraft not only found ice at the north pole, but it also found organics, which are the building blocks for life. Mercury is way too hot and airless for life as we know it, but it shows how these elements are distributed across the Solar System.")
elif option=="Venus":
    image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\venus.jpg')
    st.image(image)
    st.markdown("Venus doesn’t have any moons, and we aren’t sure why.""\nBoth Mercury and Venus have no moons, which can be considered a surprise given there are dozens of other ones around the Solar System. Saturn has over 60, for example. And some moons are little more than captured asteroids, which may have been what happened with Mars’ two moons, for example. So what makes these planets different? No one is really sure why Venus doesn’t, but there is at least one stream of research that suggests it could have had one in the past.")
elif option=="Mars":
    image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\mars.jpg')
    st.image(image)
    st.markdown("Mars had a thicker atmosphere in the past.""\nWhat a bunch of contrasts in the inner Solar System: practically atmosphere-less Mercury, a runaway hothouse greenhouse effect happening in Venus’ thick atmosphere, temperate conditions on much of Earth and then a thin atmosphere on Mars. But look at the planet and you can see gullies carved in the past from probable water. Water requires more atmosphere, so Mars had more in the past. Where did it go? Some scientists believe it’s because the Sun’s energy pushed the lighter molecules out of Mars’ atmosphere over millions of years, decreasing the thickness over time.")
elif option=="Jupiter":
    image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\jupiter.jpg')
    st.image(image)
    st.markdown("Jupiter is a great comet catcher.""\nThe most massive planet in the Solar System probably had a huge influence on its history. At 318 times the mass of Earth, you can imagine that any passing asteroid or comet going near Jupiter has a big chance of being caught or diverted. Maybe Jupiter was partly to blame for the great bombardment of small bodies that peppered our young Solar System early in its history, causing scars you can still see on the Moon today. And in 1994, astronomers worldwide were treated to a rare sight: a comet, Shoemaker-Levy 9, breaking up under Jupiter’s gravity and slamming into the atmosphere.")
elif option=="Saturn":
    image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\saturn.jpg')
    st.image(image)
    st.markdown("No one knows how old Saturn’s rings are.""\nThere’s a field of ice and rock debris circling Saturn that from afar, appear as rings. Early telescope observations of the planet in the 1600s caused some confusion: does that planet have ears, or moons, or what? With better resolution, however, it soon became clear that there was a chain of small bodies encircling the gas giant. It’s possible that a single moon tore apart under Saturn’s strong gravity and produced the rings. Or, maybe they’ve been around (pun intended) for the last few billion years, unable to coalesce into a larger body but resistant enough to gravity not to break up.")
elif option=="Uranus":
    image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\uranus.jpg')
    st.image(image)
    st.markdown("Uranus is more stormy than we thought.""\nWhen Voyager 2 flew by the planet in the 1980s, scientists saw a mostly featureless blue ball and some assumed there wasn’t much activity going on on Uranus. We’ve had a better look at the data since then that does show some interesting movement in the southern hemisphere. Additionally, the planet drew closer to the Sun in 2007, and in more recent years telescope probing has shown some storms going on. What is causing all this activity is difficult to say unless we were to send another probe that way. And unfortunately, there are no missions yet that are slated for sure to zoom out to that part of the Solar System.")
elif option=="Neptune":
    image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\neptune.jpg')
    st.image(image)
    st.markdown("Neptune has supersonic winds.""\nWhile on Earth we are concerned about hurricanes, the strength of these storms is nowhere near what you would find on Neptune. At its highest altitudes, according to NASA, winds blow at more than 1,100 miles per hour (1,770 kilometers per hour). To put that in context, that’s faster than the speed of sound on Earth, at sea level. Why Neptune is so blustery is a mystery, especially considering the Sun’s heat is so little at its distance.")
else:
    st.write("please,select an option.")
picture = st.camera_input("Take a picture of beautiful :blue[Day Sky] or Night Sky and upload it here")
if picture:
    st.image(picture)