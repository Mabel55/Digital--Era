import React, { useState, useEffect } from 'react';

import { motion } from 'framer-motion';
import { Trophy, Medal, Star, Flame, ChevronLeft, Home } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export default function Leaderboard() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  
  const token = localStorage.getItem('token');

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        // The API returns the list directly
        const response = await fetch('/leaderboard');
        if (!response.ok) throw new Error('Failed to fetch leaderboard');
        const data = await response.json();
        setUsers(data);
      } catch (error) {
        console.error("Error fetching leaderboard:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  // Framer Motion variants
  const containerVariants = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 300 } }
  };

  const getRankColor = (index) => {
    if (index === 0) return 'from-yellow-400/20 to-yellow-600/20 border-yellow-500 shadow-[0_0_20px_rgba(234,179,8,0.2)]';
    if (index === 1) return 'from-gray-300/20 to-gray-500/20 border-gray-400 shadow-[0_0_20px_rgba(156,163,175,0.2)]';
    if (index === 2) return 'from-amber-600/20 to-amber-800/20 border-amber-700 shadow-[0_0_20px_rgba(217,119,6,0.2)]';
    return 'from-slate-800/80 to-slate-900/90 border-slate-700/50';
  };

  const getRankIcon = (index) => {
    if (index === 0) return <Trophy className="w-8 h-8 text-yellow-300 drop-shadow-[0_0_8px_rgba(253,224,71,0.8)]" />;
    if (index === 1) return <Medal className="w-7 h-7 text-gray-300" />;
    if (index === 2) return <Medal className="w-7 h-7 text-amber-600" />;
    return <span className="text-xl font-bold text-slate-400">#{index + 1}</span>;
  };

  return (
    <div className="min-h-screen bg-[#0a0a0a] text-white overflow-hidden relative selection:bg-cyan-500/30">
      {/* Background glowing effects */}
      <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] rounded-full bg-cyan-900/20 blur-[120px] pointer-events-none" />
      <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] rounded-full bg-blue-900/20 blur-[120px] pointer-events-none" />

      <div className="max-w-5xl mx-auto px-4 py-12 relative z-10 pt-12">
        
        <div className="flex items-center gap-4 mb-12">
          <button 
             onClick={() => navigate(token ? '/' : '/')}
             className="p-2 bg-slate-800/50 rounded-lg hover:bg-slate-700 transition-colors border border-slate-700 flex items-center justify-center"
             title="Go Back"
          >
             {token ? <Home className="w-5 h-5 text-slate-300" /> : <ChevronLeft className="w-5 h-5 text-slate-300" />}
          </button>
          <div>
            <h1 className="text-4xl md:text-5xl font-extrabold bg-gradient-to-r from-cyan-400 to-blue-500 text-transparent bg-clip-text drop-shadow-sm mb-2">
              Global Leaderboard
            </h1>
            <p className="text-slate-400 text-lg">Top 100 students ranked by total XP.</p>
          </div>
        </div>

        {loading ? (
          <div className="flex justify-center items-center h-64">
            <div className="w-12 h-12 border-4 border-cyan-500/30 border-t-cyan-500 rounded-full animate-spin" />
          </div>
        ) : (
          <>
            {/* Top 3 Podium (Visible only on lg screens for best effect, else stack) */}
            <div className="hidden lg:flex justify-center items-end gap-6 mb-16 h-72">
              {users[1] && (
                <motion.div 
                  initial={{ opacity: 0, y: 50 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.2, duration: 0.5 }}
                  className="w-1/4 flex flex-col items-center"
                >
                  <div className="mb-4 flex flex-col items-center">
                    <span className="text-xl font-bold text-gray-300 mb-1">{users[1].full_name || users[1].email.split('@')[0] || 'User'}</span>
                    <span className="text-cyan-400 font-semibold">{users[1].xp} XP</span>
                  </div>
                  <div className="w-full h-40 bg-gradient-to-t from-gray-600/40 to-gray-800/40 rounded-t-xl border-t-4 border-gray-300 shadow-[0_0_30px_rgba(156,163,175,0.1)] flex justify-center pt-4 backdrop-blur-sm">
                    <Medal className="w-10 h-10 text-white opacity-80" />
                  </div>
                </motion.div>
              )}

              {users[0] && (
                <motion.div 
                  initial={{ opacity: 0, y: 50 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0, duration: 0.5 }}
                  className="w-1/4 flex flex-col items-center z-10"
                >
                  <div className="mb-4 flex flex-col items-center relative">
                    <div className="absolute -top-10">
                      <Trophy className="w-12 h-12 text-yellow-400 drop-shadow-[0_0_15px_rgba(250,204,21,0.8)] animate-pulse" />
                    </div>
                    <span className="text-2xl font-black text-yellow-400 mb-1 drop-shadow-md">{users[0].full_name || users[0].email.split('@')[0] || 'User'}</span>
                    <span className="text-cyan-400 font-bold">{users[0].xp} XP</span>
                  </div>
                  <div className="w-full h-56 bg-gradient-to-t from-yellow-600/40 to-yellow-800/40 rounded-t-xl border-t-4 border-yellow-300 shadow-[0_0_40px_rgba(250,204,21,0.2)] flex justify-center pt-4 backdrop-blur-sm">
                    <span className="text-4xl font-black text-white opacity-80">1</span>
                  </div>
                </motion.div>
              )}

              {users[2] && (
                <motion.div 
                  initial={{ opacity: 0, y: 50 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.4, duration: 0.5 }}
                  className="w-1/4 flex flex-col items-center"
                >
                  <div className="mb-4 flex flex-col items-center">
                    <span className="text-lg font-bold text-amber-500 mb-1">{users[2].full_name || users[2].email.split('@')[0] || 'User'}</span>
                    <span className="text-cyan-400 font-semibold">{users[2].xp} XP</span>
                  </div>
                  <div className="w-full h-32 bg-gradient-to-t from-amber-800/40 to-amber-900/40 rounded-t-xl border-t-4 border-amber-600 shadow-[0_0_30px_rgba(217,119,6,0.1)] flex justify-center pt-4 backdrop-blur-sm">
                    <Medal className="w-8 h-8 text-white opacity-80" />
                  </div>
                </motion.div>
              )}
            </div>

            {/* Full List */}
            <motion.div 
              variants={containerVariants}
              initial="hidden"
              animate="show"
              className="flex flex-col gap-3"
            >
              {users.map((user, index) => (
                <motion.div 
                  key={user.id} 
                  variants={itemVariants}
                  whileHover={{ scale: 1.01, translateX: 5 }}
                  className={`relative overflow-hidden flex items-center justify-between p-4 md:p-6 rounded-2xl border bg-gradient-to-r ${getRankColor(index)} backdrop-blur-sm transition-all`}
                >
                  {/* Subtle glass reflection */}
                  <div className="absolute inset-0 bg-white/5 opacity-0 hover:opacity-100 transition-opacity" />
                  
                  <div className="flex items-center gap-4 md:gap-6 z-10">
                    <div className="w-12 flex justify-center">
                      {getRankIcon(index)}
                    </div>
                    
                    <div className="w-10 h-10 md:w-12 md:h-12 rounded-full bg-slate-800 flex items-center justify-center border border-slate-700 shadow-inner">
                      <span className="font-bold text-lg text-cyan-400">
                        {((user.full_name || user.email) || 'U').charAt(0).toUpperCase()}
                      </span>
                    </div>

                    <div className="flex flex-col">
                      <span className="text-lg md:text-xl font-bold text-white group-hover:text-cyan-300 transition-colors">
                        {user.full_name || user.email.split('@')[0] || 'User'}
                      </span>
                      <div className="flex items-center gap-3 mt-1">
                        <span className="text-xs md:text-sm text-slate-400 font-medium px-2 py-0.5 bg-slate-800/80 rounded-md border border-slate-700">
                          {user.level || 'Novice'}
                        </span>
                        {user.streak > 0 && (
                          <span className="flex items-center text-xs md:text-sm text-orange-400 font-medium px-2 py-0.5 bg-orange-500/10 rounded-md border border-orange-500/20">
                            <Flame className="w-3 h-3 mr-1" /> {user.streak} day streak
                          </span>
                        )}
                      </div>
                    </div>
                  </div>

                  <div className="flex flex-col items-end z-10">
                    <div className="flex items-center gap-1.5 bg-slate-900/50 px-4 py-2 rounded-xl border border-slate-700/50 shadow-inner">
                      <Star className="w-5 h-5 text-cyan-400 fill-cyan-400/20" />
                      <span className="text-xl md:text-2xl font-black text-white font-mono tracking-tight">{user.xp.toLocaleString()}</span>
                      <span className="text-sm text-cyan-500 font-bold ml-1 hidden md:block">XP</span>
                    </div>
                  </div>
                </motion.div>
              ))}
            </motion.div>
          </>
        )}
      </div>
    </div>
  );
}
