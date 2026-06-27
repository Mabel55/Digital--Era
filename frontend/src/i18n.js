import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

// Basic translations (you can later move these to separate JSON files)
const resources = {
  en: {
    translation: {
      "dashboard": {
        "welcome": "Welcome back",
        "loading": "Loading...",
        "start_learning": "Start Learning",
        "courses": "Courses",
        "leaderboard": "Leaderboard"
      }
    }
  },
  es: {
    translation: {
      "dashboard": {
        "welcome": "Bienvenido de nuevo",
        "loading": "Cargando...",
        "start_learning": "Empezar a aprender",
        "courses": "Cursos",
        "leaderboard": "Tabla de clasificación"
      }
    }
  }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: "en", // default language
    fallbackLng: "en",
    interpolation: {
      escapeValue: false // react already safes from xss
    }
  });

export default i18n;
