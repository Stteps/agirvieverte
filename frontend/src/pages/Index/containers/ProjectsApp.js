import React from "react";
import PropTypes from "prop-types";
// import { useTranslation } from 'react-i18next';
import { Navigation } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";

import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/scrollbar';


const ProjectsApp = (props) => {
    // const { t } = useTranslation(["common", "glossary", "Index/IndexApp"]);

    return <>
        <Swiper modules = {[ Navigation ]}
            rewind = { true }
            navigation = { true }
            noSwiping
            noSwipingClass = 'swiper'
        >
            {
                props.projects.map((item, i) => <SwiperSlide key = { i }>
                    <div>
                        <img src = { item.picture } className = "px-5" style = {{ height: "80vh" }} />
                        <span className = "text-white m-3 fs-3 fw-bold">{ item.title.toUpperCase() }</span>
                    </div>
                </SwiperSlide>)
            }
        </Swiper>
    </>;
};

ProjectsApp.propTypes = {
    projects: PropTypes.arrayOf(PropTypes.object)
};

export default ProjectsApp;