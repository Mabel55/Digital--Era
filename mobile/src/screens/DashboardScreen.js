import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity, ActivityIndicator } from 'react-native';
import { useAuth } from '../AuthContext';
import axios from 'axios';

export default function DashboardScreen() {
  const { user, token, logout, baseURL } = useAuth();
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchCourses();
  }, []);

  const fetchCourses = async () => {
    try {
      const response = await axios.get(`${baseURL}/courses`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setCourses(response.data);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const renderCourse = ({ item }) => (
    <View style={styles.courseCard}>
      <Text style={styles.courseTitle}>{item.title || item.name}</Text>
      <Text style={styles.courseDesc} numberOfLines={2}>
        {item.description || 'Master this topic step by step.'}
      </Text>
      <View style={styles.courseMeta}>
        <Text style={styles.badge}>{item.level || 'Beginner'}</Text>
        <Text style={styles.badge}>{item.track || 'General'}</Text>
      </View>
    </View>
  );

  if (loading) {
    return (
      <View style={[styles.container, styles.centered]}>
        <ActivityIndicator size="large" color="#38bdf8" />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <View>
          <Text style={styles.greeting}>Welcome back,</Text>
          <Text style={styles.name}>{user?.full_name || user?.email.split('@')[0]}</Text>
        </View>
        <TouchableOpacity onPress={logout} style={styles.logoutBtn}>
          <Text style={styles.logoutText}>Log Out</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.statsRow}>
        <View style={styles.statBox}>
          <Text style={styles.statValue}>{user?.level || 'Beginner'}</Text>
          <Text style={styles.statLabel}>Current Level</Text>
        </View>
        <View style={styles.statBox}>
          <Text style={styles.statValue}>{user?.xp || 0}</Text>
          <Text style={styles.statLabel}>Total XP</Text>
        </View>
        <View style={styles.statBox}>
          <Text style={styles.statValue}>🔥 {user?.streak || 0}</Text>
          <Text style={styles.statLabel}>Day Streak</Text>
        </View>
      </View>

      <Text style={styles.sectionTitle}>Available Courses</Text>
      
      <FlatList
        data={courses}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderCourse}
        contentContainerStyle={{ paddingBottom: 40 }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f172a',
    paddingTop: 50,
    paddingHorizontal: 20,
  },
  centered: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 30,
  },
  greeting: {
    color: '#94a3b8',
    fontSize: 14,
  },
  name: {
    color: '#fff',
    fontSize: 24,
    fontWeight: 'bold',
  },
  logoutBtn: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    backgroundColor: 'rgba(239, 68, 68, 0.2)',
    borderRadius: 6,
  },
  logoutText: {
    color: '#ef4444',
    fontWeight: 'bold',
  },
  statsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 30,
  },
  statBox: {
    backgroundColor: '#1e293b',
    borderRadius: 12,
    padding: 16,
    flex: 1,
    alignItems: 'center',
    marginHorizontal: 4,
    borderWidth: 1,
    borderColor: '#334155',
  },
  statValue: {
    color: '#38bdf8',
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  statLabel: {
    color: '#94a3b8',
    fontSize: 12,
  },
  sectionTitle: {
    color: '#fff',
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  courseCard: {
    backgroundColor: '#1e293b',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#334155',
  },
  courseTitle: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  courseDesc: {
    color: '#94a3b8',
    fontSize: 14,
    marginBottom: 12,
  },
  courseMeta: {
    flexDirection: 'row',
    gap: 8,
  },
  badge: {
    backgroundColor: 'rgba(56, 189, 248, 0.1)',
    color: '#38bdf8',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 4,
    fontSize: 12,
    fontWeight: 'bold',
    overflow: 'hidden',
  }
});
