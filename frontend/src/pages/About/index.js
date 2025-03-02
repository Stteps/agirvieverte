import "~/scss/pages/about.scss";

import React from "react";
import { createRoot } from "react-dom/client";

import "../i18n";

import EducationGalleryApp from "./containers/EducationGalleryApp";

$(() => {
    createRoot(document.getElementById("education-gallery-app")).render(
        <EducationGalleryApp pictures = { EDUCATION_GALLERY_PICTURES } />
    );
});
