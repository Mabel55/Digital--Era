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
        "leaderboard": "Leaderboard",
        "profile": "Profile",
        "settings": "Settings",
        "logout": "Logout",
        "search": "Search courses..."
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
        "leaderboard": "Tabla de clasificación",
        "profile": "Perfil",
        "settings": "Ajustes",
        "logout": "Cerrar sesión",
        "search": "Buscar cursos..."
      }
    }
  },
  fr: {
    translation: {
      "dashboard": {
        "welcome": "Bon retour",
        "loading": "Chargement...",
        "start_learning": "Commencer à apprendre",
        "courses": "Cours",
        "leaderboard": "Classement",
        "profile": "Profil",
        "settings": "Paramètres",
        "logout": "Déconnexion",
        "search": "Rechercher des cours..."
      }
    }
  },
  ig: {
    translation: {
      "dashboard": {
        "welcome": "Nnọọ",
        "loading": "N'ebunye...",
        "start_learning": "Malite Ịmụta",
        "courses": "Ọmụmụ",
        "leaderboard": "Bọọdụ Ndị Ndú",
        "profile": "Profaịlụ",
        "settings": "Ntọala",
        "logout": "Pụọ",
        "search": "Chọọ ọmụmụ..."
      }
    }
  },
  yo: {
    translation: {
      "dashboard": {
        "welcome": "Kaabo pada",
        "loading": "N gberu...",
        "start_learning": "Bẹrẹ Ẹkọ",
        "courses": "Awọn Ẹkọ",
        "leaderboard": "Igbimọ Aṣaaju",
        "profile": "Profaili",
        "settings": "Awọn Eto",
        "logout": "Jade",
        "search": "Wa awọn ẹkọ..."
      }
    }
  },
  ha: {
    translation: {
      "dashboard": {
        "welcome": "Barka da dawowa",
        "loading": "Ana lodi...",
        "start_learning": "Fara Koyo",
        "courses": "Darussa",
        "leaderboard": "Jadawalin Jagoranci",
        "profile": "Furofayil",
        "settings": "Saituna",
        "logout": "Fita",
        "search": "Nemo darussa..."
      }
    }
  },
  sw: {
    translation: {
      "dashboard": {
        "welcome": "Karibu tena",
        "loading": "Inapakia...",
        "start_learning": "Anza Kujifunza",
        "courses": "Kozi",
        "leaderboard": "Ubao wa Viongozi",
        "profile": "Wasifu",
        "settings": "Mipangilio",
        "logout": "Toka",
        "search": "Tafuta kozi..."
      }
    }
  },
  ar: {
    translation: {
      "dashboard": {
        "welcome": "مرحباً بعودتك",
        "loading": "جاري التحميل...",
        "start_learning": "ابدأ التعلم",
        "courses": "الدورات",
        "leaderboard": "لوحة الصدارة",
        "profile": "الملف الشخصي",
        "settings": "الإعدادات",
        "logout": "تسجيل خروج",
        "search": "ابحث عن الدورات..."
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
