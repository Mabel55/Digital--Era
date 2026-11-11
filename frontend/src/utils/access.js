function parseGrants(subscription) {
  if (!subscription) return {};
  let grants = subscription.access_grants || {};
  if (typeof grants === 'string') {
    try {
      grants = JSON.parse(grants);
    } catch {
      grants = {};
    }
  }
  return typeof grants === 'object' && grants !== null ? grants : {};
}

function checkGrantMatch(grants, type, targetName) {
  if (!grants || !targetName) return false;
  const now = new Date();
  const cleanTarget = targetName.trim().toLowerCase();
  const cleanType = type.trim().toLowerCase();

  for (const [key, expiry] of Object.entries(grants)) {
    const parts = key.split(':');
    if (parts.length < 2) continue;
    const gType = parts[0].trim().toLowerCase();
    const gName = parts.slice(1).join(':').trim().toLowerCase();

    if (gType === cleanType && gName === cleanTarget) {
      if (expiry === null || expiry === undefined || new Date(expiry) > now) {
        return true;
      }
    }
  }
  return false;
}

/**
 * Checks if a user has access to a specific course.
 * 
 * @param {string} level - 'Beginner', 'Intermediate', or 'Advanced'
 * @param {string} trackName - The name of the track (e.g. 'Backend')
 * @param {string} courseName - The name of the course
 * @param {object} subscription - The user.subscription object
 * @returns {boolean} True if they have access, false otherwise
 */
export function hasAccess(level, trackName, courseName, subscription) {
  // Beginner courses are always accessible (freemium: first 3 lessons free inside)
  if (level === 'Beginner') {
    return true;
  }
  
  if (!subscription) {
    return false;
  }

  // Full Pro unlocks everything
  if (subscription.is_pro) {
    return true;
  }

  const grants = parseGrants(subscription);
  if (checkGrantMatch(grants, 'course', courseName)) return true;
  if (checkGrantMatch(grants, 'track', trackName)) return true;

  return false;
}

/**
 * Checks if a user has access to a specific lesson within a course.
 * Freemium: First 3 lessons of Beginner courses are always free.
 * 
 * @param {number} lessonIdx - 0-based lesson index
 * @param {string} level - 'Beginner', 'Intermediate', or 'Advanced'
 * @param {string} trackName - The name of the track
 * @param {string} courseName - The name of the course
 * @param {object} subscription - The user.subscription object
 * @returns {boolean} True if they have access to this lesson
 */
export function hasLessonAccess(lessonIdx, level, trackName, courseName, subscription) {
  // First 3 lessons of Beginner courses are always free (freemium)
  if (level === 'Beginner' && lessonIdx < 3) {
    return true;
  }

  if (!subscription) {
    return false;
  }

  // Pro unlocks everything
  if (subscription.is_pro) {
    return true;
  }

  const grants = parseGrants(subscription);
  if (checkGrantMatch(grants, 'course', courseName)) return true;
  if (checkGrantMatch(grants, 'track', trackName)) return true;

  return false;
}
