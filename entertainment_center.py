import fresh_tomatoes
import media

# A movie entry being given its appropriate "Title", "Synopsis", "Poster Link",
# and "Trailer Link"

the_birdcage = media.Movie("The Birdcage",
                           "In this remake of the classic French farce"
                           "\"La Cageaux Folles,\" engaged couple Val Goldman"
                           "(Dan Futterman) and Barbara Keeley"
                           "(Calista Flockhart) shakily introduce their future"
                           "in-laws. Val's father, Armand (Robin Williams), a "
                           "gay Miami drag club owner, pretends to be straight"
                           "and attempts to hide his relationship with Albert "
                           "(Nathan Lane), his life partner and the club's"
                           "flamboyant star attraction, so as to please"
                           "Barbara's father, controversial Republican Sen. "
                           "Kevin Keeley (Gene Hackman)",
                           "https://upload.wikimedia.org/wikipedia/en/7/76/Birdcage_imp.jpg",  # noqa
                           "https://www.youtube.com/watch?v=MxfXR1zSj1k")

in_and_out = media.Movie("In and Out",
                         "Upon winning an Academy Award, actor Cameron Drake"
                         "(Matt Dillon) honors his high school teacher, Howard"
                         "Brackett (Kevin Kline), who he announces, before"
                         "millions of viewers, is gay. This comes as news to"
                         "Brackett's parents (Wilford Brimley, Debbie Reynolds"
                         "), his principal (Bob Newhart) and especially his "
                         "fiancée (Joan Cusack). As a media blitz descends"
                         "upon on his small Indiana town, Brackett attempts to"
                         " convince everyone that he's your average straight "
                         "American male.",
                         "https://www.gstatic.com/tv/thumb/movieposters/19876/p19876_p_v8_ah.jpg",  # noqa
                         "https://www.youtube.com/watch?v=fxD7Ty5ZhQE")

singing_in_the_rain = media.Movie("Singin' in the Rain",
                                  "A spoof of the turmoil that afflicted the"
                                  "movie industry in the late 1920s when"
                                  "movies went from silent to sound. When two "
                                  "silent movie stars', Don Lockwood and Lina "
                                  "Lamont, latest movie is made into a musical"
                                  "  a chorus girl is brought in to dub Lina's"
                                  "speaking and singing. Don is on top of the"
                                  "world until Lina finds out.",
                                  "https://t1.gstatic.com/images?q=tbn:ANd9GcS4WcFi6lA8nOZUA42Vi5G_iyj9cNFf3kBSDIofQQSRDiO1DemA",  # noqa
                                  "https://www.youtube.com/watch?v=Lv6DNrIUiZU")  # noqa

the_grand_budapest = media.Movie("The Grand Budapest Hotel",
                                 "In the 1930s, the Grand Budapest Hotel is a"
                                 " popular European ski resort, presided over"
                                 "  by concierge Gustave H. (Ralph Fiennes)."
                                 " Zero, a junior lobby boy, becomes Gustave's"
                                 " friend and protege. Gustave prides himself"
                                 " on providing first-class service to the "
                                 "hotel's guests, including satisfying the"
                                 "sexual needs of the many elderly women who"
                                 " stay there. When one of Gustave's lovers "
                                 " dies mysteriously, Gustave finds himself "
                                 " the recipient of a priceless painting "
                                 "and the chief suspect in her murder.",
                                 "https://t0.gstatic.com/images?q=tbn:ANd9GcSDDmHpt0TcHkK9DCv0QU-Xx4WNEVOJnHlj7pVfN61-1mEX2eCG",  # noqa
                                 "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

analyze_this = media.Movie("Analyze This",
                           "When doctors tell a mob boss (Robert De Niro) that"
                           " he is suffering from anxiety attacks, he seeks"
                           " the help of Ben, a therapist (Billy Crystal) "
                           ", who is manipulated into treating him,"
                           " with hysterical results. Just as Ben and "
                           " his fiancée (Lisa Kudrow) are about to wed, they "
                           " are faced with a mobster who won't take no"
                           "for an answer.",
                           "https://www.gstatic.com/tv/thumb/movieposters/22611/p22611_p_v8_aa.jpg",  # noqa
                           "https://www.youtube.com/watch?v=z2mEgYX2pFE")

spaceballs = media.Movie("Spaceballs",
                         "In a distant galaxy, planet Spaceball has depleted"
                         "its air supply, leaving its citizens reliant on a"
                         "product called \"Perri-Air.\" In desperation,"
                         "Spaceball's leader President Skroob (Mel Brooks) "
                         "orders the evil Dark Helmet (Rick Moranis) to kidnap"
                         "Princess Vespa (Daphne Zuniga) of oxygen-rich"
                         "Druidia and hold her hostage in exchange for air. "
                         "But help arrives for the Princess in the form of"
                         " renegade space pilot Lone Starr (Bill Pullman)"
                         " and his  half-man, half-dog partner,"
                         "Barf (John Candy).",
                         "https://www.gstatic.com/tv/thumb/movieposters/10115/p10115_p_v8_an.jpg",  # noqa
                         "https://www.youtube.com/watch?v=kGIM_yNzeUo")


# The list of movies to be called by the page design
movies = [the_birdcage, in_and_out, singing_in_the_rain, the_grand_budapest,
          analyze_this, spaceballs]


# The website design from fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
