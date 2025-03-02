import React from "react";
import PropTypes from "prop-types";
// import { useTranslation } from 'react-i18next';
import { Navigation } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";

import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/scrollbar';


const EducationGalleryApp = (props) => {
    // const { t } = useTranslation(["common", "glossary", "Index/IndexApp"]);

    return <>
        <Swiper modules = {[ Navigation ]}
            rewind = { true }
            navigation = { true }
            noSwiping
            noSwipingClass = 'swiper'
        >
            {
                props.pictures.map((url, i) => <SwiperSlide key = { i }>
                    <img src = { url } className = "w-100" />
                </SwiperSlide>)
            }
        </Swiper>
    </>;
};

EducationGalleryApp.propTypes = {
    pictures: PropTypes.arrayOf(PropTypes.string)
};

export default EducationGalleryApp;