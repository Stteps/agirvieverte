import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import HttpApi from "i18next-http-backend";

i18n.use(initReactI18next).use(HttpApi).init({
    lng: document.querySelector("html").lang,
    fallbackLng: 'en',
    ns: [
        "common",
        "glossary",
        "Index/ProjectsApp",
    ],
    defaultNS: "common",
    interpolation: {
        escapeValue: false, // not needed for react as it escapes by default
    },
    backend: {
        loadPath: `${__webpack_public_path__}locales/{{lng}}/{{ns}}.${__webpack_hash__}.json`,
    },
});

export default i18n;