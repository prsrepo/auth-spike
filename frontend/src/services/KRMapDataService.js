import http from "../http-common";
class KRMapDataService {
  getAll() {
    return http.get("/krmaps");
  }
  get(id) {
    return http.get(`/krmaps/${id}`);
  }
  create(data) {
    return http.post("/krmaps", data);
  }
  update(id, data) {
    return http.put(`/krmaps/${id}`, data);
  }
  delete(id) {
    return http.delete(`/krmaps/${id}`);
  }
  deleteAll() {
    return http.delete(`/krmaps`);
  }
  findByTitle(title) {
    return http.get(`/krmaps?title=${title}`);
  }
  recentFiles() {
    return http.get("/navigate/search/recent");
  }
}
export default new KRMapDataService();
