# One School One Lab (OSOL)

#### Introduction:

<p>At present, the majority of students and teachers in Cambodia do not have access to computers at school. 

Of those schools which do have computer equipment available, the equipment is slow, inefficient, outdated, poorly designed, or obsolete. 

KOOMPI is the first notebook computer to be manufactured in Cambodia, specifically designed by and for Cambodian students, providing low-cost personal notebook computers for students, working together with integrated networking hubs for schools.

KOOMPI Co. Ltd., together with KOOMPI Academy, has designed a powerful and effective broad-based Information Technology solution, providing access to information for all students and teachers in every Cambodian school. 

The One School One Lab (OSOL) project was created to provide uniform computer workstations in over 10,000 high and junior-high schools in Cambodia.

Designed for students, teachers, and administrators, the OSOL project provides energy efficient, low maintenance, easy-to-use, cost effective Information Technology solutions for Cambodia's next generation of researchers and developers.

Each OSOL networking hub provides all the necessary hardware and software bundled together for both online and offline learning.

OSOL networking hubs are advanced learning, teaching, work and study environments, centered around a local independent server at each school.

Curriculum updates are distributed by teachers and administrators through the local server, which is uniform and compatible with all other participating schools in Cambodia.

In addition to localized curricula, together with the Ministry of Education Youth and Sport (MOEYS), and scores of participating private schools across Cambodia, KOOMPI Academy offers a fully customized work-study environment.</p>


#### How?

* Each localized OSOL network includes Raspberry Pi (RPi) integration.

* All-In-One Workstations designed to maximize energy efficiency, in a compact, powerful RPi

* Offline Content Servers (OCS) provide 24/7 data access

* One OCS per school, updated daily, or hourly, linked to Department of Information Technology (DIT) headquarters in Phnom Penh

* OCS are updated and syncronized with KOOMPI Academy for uninterupted lesson content

### Power Management Plan:

* Six 360 watt solar panels send power to two Lithium Ion batteries and controller to power the complete lab. 
 
  
* There will be a sub battery which a dedicated power supply for the local storage server, this combined with the larger battery will ensure the local network and PC's stay up during power outages.
  * The systems goal is to give 2 hours of extra run time to students using the lab. This will allow them to complete and save their class work.
  
#### Power Management Details:

> RPI = 12w
> LCD = 24w

> RPI + LCD = 36w

> set = 36w
> user = 37

> set * user = 1,332kw * 8hours = 10,656kw

> reserve = 1000kw
> lab = 10,656kw + reserve = 11,656kw  
> Total = 11,656kw

<p>Our labe will store Total in order to keep labs up and running for up-to 8 hours after power out</p>

#### AD Battery:

* This battery needs to power: 

  * 1 x RPI
  * 1 x HDD

> RPI = 12w
> HDD = 3w

> RPI + HDD = 15w

> needed = 15w
> hours = 24hours

> needed * hours = 360w
> Total = 360w

<p>One AD battery will store Total in order to give students and teachers access to saved files for 24hours after power out.</p>

#### To conclude:

<p>We aim to implement Labs in each school in Cambodia with 4 things in mind, usability, minimal internet dependency, efficiency and affordable cost. Following the plans above we will achieve each of those targets.</p>
