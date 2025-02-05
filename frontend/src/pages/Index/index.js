import React from "react";
import { createRoot } from "react-dom/client";

import "../i18n";

import ProjectsApp from "./containers/ProjectsApp";

import '~/scss/pages/index.scss';

import "~/assets/images/landing_background.jpg";
import "~/assets/images/education_thumbnail.png";
import "~/assets/images/recycling_thumbnail.png";
import "~/assets/images/agriculture_thumbnail.png";
import "~/assets/images/health_thumbnail.png";
import "~/assets/images/renewable_thumbnail.png";
import "~/assets/images/digital_thumbnail.png";
import "~/assets/images/housing_thumbnail.png";

import logo from "~/assets/images/logo.png";
import logo_dark from "~/assets/images/logo_dark.png";

$("body").css("background", `fixed no-repeat center url(${LANDING_BANNER})`);
$("body").css("background-size", "cover");
$("#landing").css("background", "rgba(0, 0, 0, 50%");

window.onload = () => {
  const navDomElement = document.querySelector('nav');
  if (window.pageYOffset == 0) {
    navDomElement.classList.remove('bg-white', 'shadow');
    navDomElement.classList.add('py-3', 'navbar-dark', 'blurred-background');
  } else {
    navDomElement.classList.remove('opacity-0', "navbar-dark");
  }
  
  window.addEventListener('scroll', () => {
    if (window.pageYOffset == 0) {
      navDomElement.classList.remove('bg-white', 'shadow');
      navDomElement.classList.add('py-3', 'navbar-dark');
      setTimeout(() => { navDomElement.classList.add('blurred-background'); }, 50);
      $(".navbar-brand img").attr("src", logo_dark);
    } else {
      navDomElement.classList.add('bg-white', 'shadow');
      navDomElement.classList.remove('py-3', 'opacity-0', 'navbar-dark', 'blurred-background');
      $(".navbar-brand img").attr("src", logo);
    }
  });

  setTimeout(() => {
    navDomElement.classList.remove('opacity-0');
  }, 1500);

  createRoot(document.getElementById("projects-app")).render(
    <ProjectsApp
      projects = { PROJECTS }
    />
  );
};


