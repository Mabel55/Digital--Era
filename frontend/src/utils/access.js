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
  // Beginner courses are always free
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

  // Check specific access grants
  const grants = subscription.access_grants || {};
  
  const now = new Date();
  
  // Check course grant
  const courseGrant = grants[`course:${courseName}`];
  if (courseGrant !== undefined) {
    if (courseGrant === null || new Date(courseGrant) > now) {
      return true;
    }
  }

  // Check track grant
  const trackGrant = grants[`track:${trackName}`];
  if (trackGrant !== undefined) {
    if (trackGrant === null || new Date(trackGrant) > now) {
      return true;
    }
  }

  return false;
}
